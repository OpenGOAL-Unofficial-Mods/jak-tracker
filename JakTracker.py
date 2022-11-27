from OpenGoalAutoTracker import OpenGoalAutoTracker
from PIL import Image 
import io
import time
import PySimpleGUI as PSG

# layout for tracker UI
LAYOUT = [
  [ # totals & misc
    'num_power_cells',
    'num_orbs',
    'num_scout_flies',
    # 'blank',
    # 'res_jungle_eggtop',
    # 'res_jungle_fishgame',
    # 'res_snow_eggtop',
  ],
  'HSeparator',
  [ # Geyser Rock
    'res_training_gimmie',
    'res_training_door',
    'res_training_climb',
    'res_training_buzzer',
  ],
  [ # Sandover Village
    'res_village1_mayor_money',
    'res_village1_uncle_money',
    'res_village1_yakow',
    'res_village1_oracle_money1',
    'res_village1_oracle_money2',
    'res_village1_buzzer',
  ],
  [ # Sentinel Beach
    'res_beach_ecorocks',
    'res_beach_flutflut',
    'res_beach_pelican',
    'res_beach_seagull',
    'res_beach_cannon',
    'res_beach_gimmie',
    'res_beach_sentinel',
    'res_beach_buzzer',
  ],
  [ # Forbidden Jungle
    'res_jungle_lurkerm', # mirrors
    'res_jungle_tower',
    'res_jungle_eggtop',  # blue eco switch
    'res_jungle_plant',
    'res_jungle_fishgame',
    'res_jungle_canyon_end',
    'res_jungle_temple_door',
    'res_jungle_buzzer',
  ],
  [ # Misty Island
    'res_misty_muse',
    'res_misty_boat', # top of lurker ship
    'res_misty_cannon',
    'res_misty_warehouse', # return to dark eco pool
    'res_misty_bike', # flying lurkers
    'res_misty_bike_jump',  # zoomer jump
    'res_misty_eco_challenge',  # boosted
    'res_misty_buzzer',
  ],
  [ # Fire Canyon
    'res_firecanyon_end',
    'res_firecanyon_buzzer',
  ],
  [ # Rock Village
    'res_village2_gambler_money',
    'res_village2_geologist_money',
    'res_village2_warrior_money',
    'res_village2_oracle_money1',
    'res_village2_oracle_money2',
    'res_village2_buzzer',
  ],
  [ # Lost Precusor City
    'res_sunken_room',  # raise the chamber
    'res_sunken_pipe',  # pipegame
    'res_sunken_slide', # bottom of LPC
    'res_sunken_sharks',  # quickly cross dangerous pool (next to button skip)
    'res_sunken_platforms', # puzzle
    'res_sunken_top_of_helix',  # climb from bottom (piggyback)
    'res_sunken_spinning_room', # center of the complex (above dark eco)
    'res_sunken_buzzer',
  ],
  [ # Boggy Swamp
    'res_swamp_flutflut',
    'res_swamp_billy',
    'res_swamp_battle',
    'res_swamp_tether_4', # yep this is the order in start menu >_<
    'res_swamp_tether_1',
    'res_swamp_tether_2',
    'res_swamp_tether_3',
    'res_swamp_buzzer',
  ],
  [ # Precursor Basin
    'res_rolling_moles',
    'res_rolling_robbers',
    'res_rolling_race',
    'res_rolling_lake',
    'res_rolling_plants',
    'res_rolling_ring_chase_1',
    'res_rolling_ring_chase_2',
    'res_rolling_buzzer',
  ],
  [ # Mountain Pass
    'res_ogre_boss',  # klaww
    'res_ogre_end',
    'res_ogre_secret',  # backwards cell / stalag hops / tree hops / boulder skip
    'res_ogre_buzzer',
  ],
  [ # Volcanic Crater
    'res_village3_miner_money1',
    'res_village3_miner_money2',
    'res_village3_miner_money3',
    'res_village3_miner_money4',
    'res_village3_oracle_money1',
    'res_village3_oracle_money2',
    'res_village3_extra1',  # secret cell (from spider cave)
    'res_village3_buzzer',
  ],
  [ # Snowy Mountain
    'res_snow_eggtop',  # yellow eco switch
    'res_snow_ram', # lurker troops
    'res_snow_bumpers', # blockers
    'res_snow_cage',  # frozen crate (yellow eco/flutflut)
    'res_snow_fort',  # inside fortress
    'res_snow_ball',  # open fortress gate
    'res_snow_bunnies',
    'res_snow_buzzer',
  ],
  [ # Spider Cave
    'res_cave_gnawers',
    'res_cave_dark_crystals',
    'res_cave_dark_climb',
    'res_cave_robot_climb',
    'res_cave_swing_poles',
    'res_cave_spider_tunnel',
    'res_cave_platforms', # quad jump
    'res_cave_buzzer',
  ],
  [ # Lava Tube
    'res_lavatube_end',
    'res_lavatube_buzzer',
  ],
  [ # Citadel
    'res_citadel_sage_blue',
    'res_citadel_sage_red',
    'res_citadel_sage_yellow',
    'res_citadel_sage_green',
    'res_citadel_buzzer',
  ]
]

# config for fields to query
offset_tmp = 0
FIELDS = {
  'num_power_cells': {
    'display': 'POWER CELLS',
    'icon_type': 'counter',
    'icons': [
      'cell_counter.png',
    ],
    'offset': offset_tmp,
    'length': 4,
  },
  'num_orbs': {
    'display': 'PRECURSOR ORBS (TOTAL)',
    'icon_type': 'counter',
    'icons': [
      'orb_counter.png',
    ],
    'offset': (offset_tmp:=offset_tmp+4),
    'length': 4,
  },
  'num_scout_flies': {
    'display': 'SCOUT FLIES (TOTAL)',
    'icon_type': 'counter',
    'icons': [
      'fly_counter.png',
    ],
    'offset': (offset_tmp:=offset_tmp+4),
    'length': 4,
  },
  'padding_stats': {
    'display': 'padding_stats',
    'icon_type': 'skip',
    'offset': (offset_tmp:=offset_tmp+4),
    'length': 200,
  },
  'game_hash': {
    'display': 'game_hash',
    'icon_type': 'skip',
    'offset': (offset_tmp:=offset_tmp+200), # 212
    'length': 4,
  },
  'in_cutscene': {
    'display': 'in_cutscene',
    'icon_type': 'skip',
    'offset': (offset_tmp:=offset_tmp+4),
    'length': 4,
  },
  'is_loading': {
    'display': 'is_loading',
    'icon_type': 'skip',
    'offset': (offset_tmp:=offset_tmp+4),
    'length': 4,
  },
  'padding_controls': {
    'display': 'padding_controls',
    'icon_type': 'skip',
    'offset': (offset_tmp:=offset_tmp+4),
    'length': 200,
  },
  'res_training_gimmie': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_training_gimmie.png',
    ],
    'offset': (offset_tmp:=offset_tmp+200), # 424
    'length': 1,
  },
  'res_training_door': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_training_door.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_training_climb': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_training_climb.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_training_buzzer': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      '7flies_cell.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_jungle_eggtop': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_jungle_eggtop.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_jungle_lurkerm': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_jungle_lurkerm.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_jungle_tower': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_jungle_tower.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_jungle_fishgame': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_jungle_fish.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_jungle_plant': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_jungle_plant.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_jungle_buzzer': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      '7flies_cell.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_jungle_canyon_end': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_jungle_canyon_end.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_jungle_temple_door': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_jungle_temple_door.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_village1_yakow': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_village1_yakow.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_village1_mayor_money': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_village1_mayor_money.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_village1_uncle_money': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_village1_uncle_money.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_village1_oracle_money1': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_village1_oracle_money1.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_village1_oracle_money2': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_village1_oracle_money2.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_village1_buzzer': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      '7flies_cell.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_beach_ecorocks': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_beach_ecorocks.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_beach_pelican': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_beach_pelican.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_beach_flutflut': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_beach_flutflut.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_beach_seagull': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_beach_seagull.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_beach_cannon': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_beach_cannon.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_beach_buzzer': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      '7flies_cell.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_beach_gimmie': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_beach_gimmie.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_beach_sentinel': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_beach_sentinel.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_misty_muse': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_misty_muse.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_misty_boat': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_misty_boat.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_misty_warehouse': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_misty_warehouse.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_misty_cannon': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_misty_cannon.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_misty_bike': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_misty_bike.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_misty_buzzer': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      '7flies_cell.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_misty_bike_jump': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_misty_bike_jump.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_misty_eco_challenge': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_misty_eco_challenge.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_village2_gambler_money': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_village2_gambler_money.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_village2_geologist_money': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_village2_geologist_money.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_village2_warrior_money': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_village2_warrior_money.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_village2_oracle_money1': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_village2_oracle_money1.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_village2_oracle_money2': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_village2_oracle_money2.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_village2_buzzer': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      '7flies_cell.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_swamp_billy': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_swamp_billy.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_swamp_flutflut': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_swamp_flutflut.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_swamp_battle': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_swamp_battle.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_swamp_tether_1': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_swamp_tether_1.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_swamp_tether_2': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_swamp_tether_2.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_swamp_tether_3': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_swamp_tether_3.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_swamp_tether_4': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_swamp_tether_4.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_swamp_buzzer': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      '7flies_cell.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_swamp_arm': {
    'display': 'GET TO THE CENTER OF THE SWAMP',  # ayo?
    'icon_type': 'skip',
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_sunken_platforms': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_sunken_platforms.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_sunken_pipe': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_sunken_pipe.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_sunken_slide': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_sunken_slide.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_sunken_room': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_sunken_room.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_sunken_sharks': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_sunken_sharks.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_sunken_buzzer': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      '7flies_cell.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_sunken_top_of_helix': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_sunken_top_of_helix.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_sunken_spinning_room': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_sunken_spinning_room.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_rolling_race': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_rolling_race.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_rolling_robbers': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_rolling_robbers.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_rolling_moles': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_rolling_moles.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_rolling_plants': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_rolling_plants.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_rolling_lake': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_rolling_lake.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_rolling_buzzer': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      '7flies_cell.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_rolling_ring_chase_1': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_rolling_ring_chase_1.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_rolling_ring_chase_2': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_rolling_ring_chase_2.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_snow_eggtop': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_snow_eggtop.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_snow_ram': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_snow_ram.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_snow_fort': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_snow_fort.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_snow_ball': {
    'display': 'OPEN THE LURKER FORT GATE',
    'icon_type': 'cell',
    'icons': [
      'res_snow_ball.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_snow_bunnies': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_snow_bunnies.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_snow_buzzer': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      '7flies_cell.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_snow_bumpers': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_snow_bumpers.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_snow_cage': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_snow_cage.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_red_eggtop': {
    'display': '',
    'icon_type': 'skip',
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_firecanyon_buzzer': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      '7flies_cell.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_firecanyon_end': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_firecanyon_end.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_citadel_sage_green': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_citadel_sage_green.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_citadel_sage_blue': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_citadel_sage_blue.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_citadel_sage_red': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_citadel_sage_red.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_citadel_sage_yellow': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_citadel_sage_yellow.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_citadel_buzzer': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      '7flies_cell.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_village3_extra1': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_village3_extra1.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_village3_buzzer': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      '7flies_cell.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_village3_miner_money1': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_village3_miner_money1.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_village3_miner_money2': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_village3_miner_money2.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_village3_miner_money3': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_village3_miner_money3.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_village3_miner_money4': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_village3_miner_money4.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_village3_oracle_money1': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_village3_oracle_money1.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_village3_oracle_money2': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_village3_oracle_money2.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_cave_gnawers': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_cave_gnawers.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_cave_dark_crystals': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_cave_dark_crystals.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_cave_dark_climb': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_cave_dark_climb.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_cave_robot_climb': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_cave_robot_climb.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_cave_swing_poles': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_cave_swing_poles.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_cave_spider_tunnel': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_cave_spider_tunnel.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_cave_platforms': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_cave_platforms.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_cave_buzzer': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      '7flies_cell.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_ogre_boss': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_ogre_boss.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_ogre_end': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_ogre_end.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_ogre_buzzer': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      '7flies_cell.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_ogre_secret': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_ogre_secret.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_lavatube_end': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      'res_lavatube_end.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_lavatube_buzzer': {
    'display': '',
    'icon_type': 'cell',
    'icons': [
      '7flies_cell.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_lavatube_balls': {
    'display': '',
    'icon_type': 'skip',
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_intro': {
    'display': '',
    'icon_type': 'skip',
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'int_finalboss_movies': {
    'display': '',
    'icon_type': 'skip',
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'unk_finalboss_movies': {
    'display': '',
    'icon_type': 'skip',
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'int_jungle_fishgame': {
    'display': '',
    'icon_type': 'skip',
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  }
}

# takes in a PIL.Image and returns the raw bytes for use in PySimpleGui
def PilImageToBytesAlpha(img, alpha: int):
  img2 = img.copy()
  img2.putalpha(alpha)
  img.paste(img2, img)
  img_byte_arr = io.BytesIO()
  img.save(img_byte_arr, format='PNG')
  return img_byte_arr.getvalue()

# reduce fields we lookup to those shown in layout
FIELDS_REDUCED = {}
for key in FIELDS:
  for row in LAYOUT:
    if key in row:
      FIELDS_REDUCED[key] = FIELDS[key]
      break

# get the auto tracker started
OGAT = OpenGoalAutoTracker()

# setup window
PSG_LAYOUT = []
for row in LAYOUT:
  psg_row = []
  if row == "HSeparator":
    psg_row.append(PSG.HSeparator())
  else:  
    for element in row:
      if element == 'blank':
        psg_row.append(PSG.Image(size=(64,64), background_color="black"))
      elif element in FIELDS:
        field_info = FIELDS[element]
        if field_info['icon_type'] == 'cell':
          # show icon for this cell
          img = Image.open('icons/' + field_info['icons'][0]).convert('RGBA')
          psg_row.append(PSG.Image(source=PilImageToBytesAlpha(img, 63), background_color="black", key=element))
        elif field_info['icon_type'] == 'counter':
          psg_row.append(PSG.Image(source='icons/' + field_info['icons'][0], background_color="black", key=element))
          psg_row.append(PSG.Text('0', size=(4,1), background_color="black", key=element+'_counter'))
      else:
        print(f'ERROR: invalid layout config for {element}')
  PSG_LAYOUT.append(psg_row)

WINDOW = PSG.Window('OpenGOAL Tracker', PSG_LAYOUT, font=('Arial', 36), background_color="black", finalize=True)
WINDOW.refresh()

# display/refresh loop
while True:
  WINDOW.refresh()
  time.sleep(0.1) # refresh 10x per sec
  # continue
  values = OGAT.read_field_values(FIELDS_REDUCED)
  for key in values:
    if key in FIELDS_REDUCED:
      field_info = FIELDS_REDUCED[key]
      if field_info['icon_type'] == 'cell':
        # show icon for this cell
        img = Image.open('icons/' + field_info['icons'][0]).convert('RGBA')
        if values[key] == 0:
          # use low opacity if not collected
          WINDOW[key].update(source=PilImageToBytesAlpha(img, 63))
        else:
          WINDOW[key].update(source=PilImageToBytesAlpha(img, 255))
      elif field_info['icon_type'] == 'counter':
        # update counter value
        WINDOW[key+'_counter'].update(values[key])
      else:
        print(f'ERROR: unrecognized value returned from autotracker {key}')