from OpenGoalAutoTracker import OpenGoalAutoTracker
from PIL import Image
import yaml
import os
import io
import time
import PySimpleGUI as PSG

# takes in a PIL.Image and returns the raw bytes for use in PySimpleGui
def pil_to_bytes_with_alpha(img, alpha: int):
  img2 = img.copy()
  img2.putalpha(alpha)
  img.paste(img2, img)
  img_byte_arr = io.BytesIO()
  img.save(img_byte_arr, format='PNG')
  return img_byte_arr.getvalue()

class JakTracker(object):
  def window_toggle_loading(self, showLoading: bool):
    if showLoading:
      self.window['loading'].update(visible=True)
      self.window['loading'].unhide_row()
      self.window['main'].update(visible=False)
      self.window['main'].hide_row()
    else:
      self.window['loading'].update(visible=False)
      self.window['loading'].hide_row()
      self.window['main'].update(visible=True)
      self.window['main'].unhide_row()

    self.window.refresh()

  def build_window(self, filename: str):
    # parse prefs from yaml file
    with open('prefs.yaml', 'r') as prefs_yaml:
      self.prefs = yaml.load(prefs_yaml, Loader=yaml.FullLoader)

    if filename == '' and self.layout is None:
      # initial window build, use defaults (otherwise empty str -> reload current layout)
      filename = self.prefs['default_layout']

    if filename != '':
      # parse self.layout from yaml file
      self.layout = []
      with open(f'layouts/{filename}', 'r') as layout_yaml:
        self.layout = yaml.load(layout_yaml, Loader=yaml.FullLoader)

    # reduce fields we lookup to those shown in layout
    self.fields_reduced = {}
    for key in self.fields:
      for row in self.layout:
        if key in row:
          self.fields_reduced[key] = self.fields[key]
          break

    # setup window
    tmp_layout = [
      [PSG.Text('Loading...', visible=True, key='loading', background_color=self.prefs['bg_color'], font=(self.prefs['counter_font_name'], self.prefs['counter_font_size']), text_color=self.prefs['counter_font_color'])]
    ]
    tmp_rows = []
    for row in self.layout:
      psg_row = []
      if row == 'HSeparator':
        psg_row.append(PSG.HSeparator(key='HSeparator'))
      else:  
        for element in row:
          if element in self.fields:
            field_info = self.fields[element]
            if field_info['field_type'] == 'boolean':
              # show icon for this cell
              img = Image.open('icons/' + field_info['icons'][0]).convert('RGBA')
              metadata = {'value': False}
              psg_row.append(PSG.Image(source=pil_to_bytes_with_alpha(img, self.prefs['uncollected_transparency']), background_color=self.prefs['bg_color'], subsample=self.prefs['icon_shrink_factor'], metadata=metadata, key=element, enable_events=(self.prefs['tracker_mode']=='manual')))
            elif field_info['field_type'] == 'counter':
              # show icon and counter
              metadata = {'count': 0}
              psg_row.append(PSG.Image(source='icons/' + field_info['icons'][0], background_color=self.prefs['bg_color'], subsample=self.prefs['icon_shrink_factor'], metadata=metadata, key=element, enable_events=(self.prefs['tracker_mode']=='manual')))
              psg_row.append(PSG.Text('0', size=(4,1), background_color=self.prefs['bg_color'], font=(self.prefs['counter_font_name'], self.prefs['counter_font_size']), text_color=self.prefs['counter_font_color'], key=element+'_counter', enable_events=(self.prefs['tracker_mode']=='manual')))
            elif field_info['field_type'] == 'string':
              psg_row.append(PSG.Text('', size=(6,1), background_color=self.prefs['bg_color'], font=(self.prefs['counter_font_name'], self.prefs['counter_font_size']), text_color=self.prefs['counter_font_color'], key=element))
          elif element[0] == '$':
            # $ first character indicates a text label
            if 'label_fixed_width' in self.prefs:
              # fixed width
              psg_row.append(PSG.Text(element[1:], size=(self.prefs['label_fixed_width'],1), background_color=self.prefs['bg_color'], font=(self.prefs['label_font_name'], self.prefs['label_font_size']), text_color=self.prefs['label_font_color'], key=element))
            else:
              # dynamic width
              psg_row.append(PSG.Text(element[1:], background_color=self.prefs['bg_color'], font=(self.prefs['label_font_name'], self.prefs['label_font_size']), text_color=self.prefs['label_font_color'], key=element))
          else:
            print(f'ERROR: invalid layout config for {element}')
      tmp_rows.append(psg_row)
    tmp_layout.append([PSG.Column(tmp_rows, visible=False, background_color=self.prefs['bg_color'], key='main')])

    # build right click menu
    layouts_submenu = list(map(lambda x: f'{x}::LAYOUT#{x}', os.listdir('layouts')))
    rc_menu = ['', ['Choose Layout', layouts_submenu, 'Reset Layout']]
    
    # cleanup/replace previous self.window, if any
    location = (50,50)
    if self.window is not None:
      location = self.window.current_location()
      self.window.close()

    # build window
    tmp_window = PSG.Window('OpenGOAL Tracker', tmp_layout, icon='appicon.ico', return_keyboard_events=True, location=location, background_color=self.prefs['bg_color'], finalize=True, right_click_menu=rc_menu)
    tmp_window.refresh()

    self.window = tmp_window
    self.window.bind('<Key-Shift_L>', 'Shift_Down')
    self.window.bind('<Key-Shift_R>', 'Shift_Down')

  def __init__(self):
    # parse fields from yaml file, convert to dictionary
    with open('fields.yaml', 'r') as fields_yaml:
      self.fields = {fld['name']:fld for fld in yaml.load(fields_yaml, Loader=yaml.FullLoader)}

    # build window - empty string uses default_layout
    self.layout = None
    self.window = None
    self.autotracker = None
    self.build_window('')
    shift = False

    # display/refresh loop
    while True:
      # handle any events
      event, values = self.window.read(timeout=100) # only refresh up to 10x per sec
      if event == PSG.WIN_CLOSED:
        break
      elif event == 'Shift_Down':
        shift = True
      elif event == 'Shift_L:16':
        shift = False
      elif event == 'Reset Layout':
        self.build_window('') # empty layout -> refresh the current one
      elif '::' in event:
        # right click menu
        tokens = event.split('::')
        if len(tokens) > 1 and len(tokens[1]) > 7 and tokens[1][:7] == 'LAYOUT#':
          # user changed the layout
          selected_layout = tokens[1][7:]
          self.build_window(selected_layout)
        else:
          print(f'unknown right click event: {event}')
      elif event != '__TIMEOUT__' and self.prefs['tracker_mode'] == 'manual':
        if len(event)>8 and event[len(event)-8:] == '_counter':
          # if *_counter clicked, just pretend the image was clicked
          event = event[:len(event)-8]

        # assume they manually toggled something
        if event in self.fields_reduced:
          field_info = self.fields_reduced[event]
          icon = self.window[event]

          if field_info['field_type'] == 'boolean':
            # toggle collected state
            icon.metadata['value'] = not icon.metadata['value']

            # update icon for this boolean
            img = Image.open('icons/' + field_info['icons'][0]).convert('RGBA')
            if icon.metadata['value']:
              self.window[event].update(source=pil_to_bytes_with_alpha(img, 255), subsample=self.prefs['icon_shrink_factor'])
            else:
              # use low opacity if not collected
              self.window[event].update(source=pil_to_bytes_with_alpha(img, self.prefs['uncollected_transparency']), subsample=self.prefs['icon_shrink_factor'])
          elif field_info['field_type'] == 'counter':
            if shift:
              # decrement count
              icon.metadata['count'] -= 1
            else:
              # increment count
              icon.metadata['count'] += 1

            # update counter value
            self.window[event+'_counter'].update(icon.metadata['count'])

      if self.prefs['tracker_mode'] == 'auto' and self.autotracker is None:
        # connect autotracker
        self.autotracker = OpenGoalAutoTracker()
      elif self.prefs['tracker_mode'] == 'manual':
        # make sure loading panel is hidden
        self.window_toggle_loading(False)

      if self.prefs['tracker_mode'] == 'auto':
        # update from autotracker
        match self.autotracker.status:
          case 'wakeup':
            # need to connect and find markers the first time
            self.window_toggle_loading(True)
            self.autotracker.find_markers(True)
          case 'no_gk':
            # gk.exe not found, let user retry
            self.window_toggle_loading(True)
            ans = PSG.popup_yes_no('Couldn''t find OpenGOAL process (gk.exe)! Try again?', icon='appicon.ico', title='Info', text_color=self.prefs['label_font_color'], background_color=self.prefs['bg_color'], keep_on_top=True)
            if ans == 'Yes':
              # this might still fail, will catch in next loop iteration
              self.autotracker.find_markers(True)
            else:
              break
          case 'connected':
            # connected but still looking for marker address, keep waiting
            self.window_toggle_loading(True)
          case 'no_marker':
            # marker address not found, let user retry
            self.window_toggle_loading(True)
            ans = PSG.popup_yes_no('Couldn''t successfully read OpenGOAL memory! Try again?', icon='appicon.ico', title='Info', text_color=self.prefs['label_font_color'], background_color=self.prefs['bg_color'], keep_on_top=True)
            if ans == 'Yes':
              # this might still fail, will catch in next loop iteration
              self.autotracker.find_markers(True)
            else:
              break
          case 'marker':
            # yay we can proceed
            self.window_toggle_loading(False)

            values = self.autotracker.read_field_values(self.fields_reduced)
            if values is not None:
              for key in values:
                if key in self.fields_reduced:
                  field_info = self.fields_reduced[key]
                  if field_info['field_type'] == 'boolean':
                    # show icon for this boolean
                    img = Image.open('icons/' + field_info['icons'][0]).convert('RGBA')
                    if values[key] == 0:
                      # use low opacity if not collected
                      self.window[key].update(source=pil_to_bytes_with_alpha(img, self.prefs['uncollected_transparency']), subsample=self.prefs['icon_shrink_factor'])
                    else:
                      self.window[key].update(source=pil_to_bytes_with_alpha(img, 255), subsample=self.prefs['icon_shrink_factor'])
                  elif field_info['field_type'] == 'counter':
                    # update counter value
                    self.window[key+'_counter'].update(values[key])
                  elif field_info['field_type'] == 'string' and key in self.window.key_dict.keys():
                    self.window[key].update(values[key])
                  else:
                    print(f'ERROR: unrecognized value returned from autotracker {key} with type {field_info["field_type"]}')

    self.window.close()

JakTracker()