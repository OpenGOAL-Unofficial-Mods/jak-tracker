from OpenGoalAutoTracker import OpenGoalAutoTracker
from PIL import Image
import yaml
import io
import time
import PySimpleGUI as PSG

# config for fields to query
offset_tmp = 0
FIELDS = {
  'num_power_cells': {
    'display': 'POWER CELLS',
    'field_type': 'counter',
    'icons': [
      'cell_counter.png',
    ],
    'offset': offset_tmp,
    'length': 4,
  },
  'num_orbs': {
    'display': 'PRECURSOR ORBS (TOTAL)',
    'field_type': 'counter',
    'icons': [
      'orb_counter.png',
    ],
    'offset': (offset_tmp:=offset_tmp+4),
    'length': 4,
  },
  'num_scout_flies': {
    'display': 'SCOUT FLIES (TOTAL)',
    'field_type': 'counter',
    'icons': [
      'fly_counter.png',
    ],
    'offset': (offset_tmp:=offset_tmp+4),
    'length': 4,
  },
  'padding_stats': {
    'display': 'padding_stats',
    'field_type': 'skip',
    'offset': (offset_tmp:=offset_tmp+4),
    'length': 200,
  },
  'game_hash': {
    'display': 'game_hash',
    'field_type': 'skip',
    'offset': (offset_tmp:=offset_tmp+200), # 212
    'length': 4,
  },
  'in_cutscene': {
    'display': 'in_cutscene',
    'field_type': 'skip',
    'offset': (offset_tmp:=offset_tmp+4),
    'length': 4,
  },
  'is_loading': {
    'display': 'is_loading',
    'field_type': 'skip',
    'offset': (offset_tmp:=offset_tmp+4),
    'length': 4,
  },
  'padding_controls': {
    'display': 'padding_controls',
    'field_type': 'skip',
    'offset': (offset_tmp:=offset_tmp+4),
    'length': 200,
  },
  'res_training_gimmie': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_training_gimmie.png',
    ],
    'offset': (offset_tmp:=offset_tmp+200), # 424
    'length': 1,
  },
  'res_training_door': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_training_door.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_training_climb': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_training_climb.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_training_buzzer': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_training_buzzer.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_jungle_eggtop': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_jungle_eggtop.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_jungle_lurkerm': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_jungle_lurkerm.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_jungle_tower': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_jungle_tower.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_jungle_fishgame': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_jungle_fish.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_jungle_plant': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_jungle_plant.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_jungle_buzzer': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_jungle_buzzer.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_jungle_canyon_end': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_jungle_canyon_end.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_jungle_temple_door': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_jungle_temple_door.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_village1_yakow': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_village1_yakow.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_village1_mayor_money': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_village1_mayor_money.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_village1_uncle_money': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_village1_uncle_money.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_village1_oracle_money1': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_village1_oracle_money1.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_village1_oracle_money2': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_village1_oracle_money2.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_village1_buzzer': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_village1_buzzer.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_beach_ecorocks': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_beach_ecorocks.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_beach_pelican': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_beach_pelican.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_beach_flutflut': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_beach_flutflut.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_beach_seagull': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_beach_seagull.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_beach_cannon': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_beach_cannon.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_beach_buzzer': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_beach_buzzer.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_beach_gimmie': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_beach_gimmie.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_beach_sentinel': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_beach_sentinel.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_misty_muse': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_misty_muse.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_misty_boat': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_misty_boat.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_misty_warehouse': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_misty_warehouse.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_misty_cannon': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_misty_cannon.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_misty_bike': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_misty_bike.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_misty_buzzer': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_misty_buzzer.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_misty_bike_jump': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_misty_bike_jump.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_misty_eco_challenge': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_misty_eco_challenge.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_village2_gambler_money': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_village2_gambler_money.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_village2_geologist_money': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_village2_geologist_money.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_village2_warrior_money': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_village2_warrior_money.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_village2_oracle_money1': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_village2_oracle_money1.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_village2_oracle_money2': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_village2_oracle_money2.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_village2_buzzer': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_village2_buzzer.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_swamp_billy': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_swamp_billy.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_swamp_flutflut': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_swamp_flutflut.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_swamp_battle': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_swamp_battle.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_swamp_tether_1': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_swamp_tether_1.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_swamp_tether_2': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_swamp_tether_2.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_swamp_tether_3': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_swamp_tether_3.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_swamp_tether_4': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_swamp_tether_4.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_swamp_buzzer': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_swamp_buzzer.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_swamp_arm': {
    'display': 'GET TO THE CENTER OF THE SWAMP',  # ayo?
    'field_type': 'skip',
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_sunken_platforms': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_sunken_platforms.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_sunken_pipe': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_sunken_pipe.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_sunken_slide': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_sunken_slide.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_sunken_room': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_sunken_room.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_sunken_sharks': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_sunken_sharks.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_sunken_buzzer': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_sunken_buzzer.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_sunken_top_of_helix': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_sunken_top_of_helix.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_sunken_spinning_room': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_sunken_spinning_room.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_rolling_race': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_rolling_race.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_rolling_robbers': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_rolling_robbers.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_rolling_moles': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_rolling_moles.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_rolling_plants': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_rolling_plants.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_rolling_lake': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_rolling_lake.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_rolling_buzzer': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_rolling_buzzer.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_rolling_ring_chase_1': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_rolling_ring_chase_1.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_rolling_ring_chase_2': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_rolling_ring_chase_2.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_snow_eggtop': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_snow_eggtop.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_snow_ram': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_snow_ram.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_snow_fort': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_snow_fort.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_snow_ball': {
    'display': 'OPEN THE LURKER FORT GATE',
    'field_type': 'cell',
    'icons': [
      'res_snow_ball.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_snow_bunnies': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_snow_bunnies.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_snow_buzzer': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_snow_buzzer.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_snow_bumpers': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_snow_bumpers.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_snow_cage': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_snow_cage.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_red_eggtop': {
    'display': '',
    'field_type': 'skip',
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_firecanyon_buzzer': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_firecanyon_buzzer.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_firecanyon_end': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_firecanyon_end.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_citadel_sage_green': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_citadel_sage_green.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_citadel_sage_blue': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_citadel_sage_blue.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_citadel_sage_red': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_citadel_sage_red.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_citadel_sage_yellow': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_citadel_sage_yellow.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_citadel_buzzer': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_citadel_buzzer.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_village3_extra1': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_village3_extra1.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_village3_buzzer': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_village3_buzzer.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_village3_miner_money1': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_village3_miner_money1.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_village3_miner_money2': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_village3_miner_money2.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_village3_miner_money3': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_village3_miner_money3.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_village3_miner_money4': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_village3_miner_money4.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_village3_oracle_money1': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_village3_oracle_money1.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_village3_oracle_money2': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_village3_oracle_money2.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_cave_gnawers': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_cave_gnawers.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_cave_dark_crystals': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_cave_dark_crystals.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_cave_dark_climb': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_cave_dark_climb.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_cave_robot_climb': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_cave_robot_climb.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_cave_swing_poles': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_cave_swing_poles.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_cave_spider_tunnel': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_cave_spider_tunnel.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_cave_platforms': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_cave_platforms.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_cave_buzzer': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_cave_buzzer.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_ogre_boss': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_ogre_boss.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_ogre_end': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_ogre_end.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_ogre_buzzer': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_ogre_buzzer.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_ogre_secret': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_ogre_secret.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_lavatube_end': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_lavatube_end.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_lavatube_buzzer': {
    'display': '',
    'field_type': 'cell',
    'icons': [
      'res_lavatube_buzzer.png',
    ],
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_lavatube_balls': {
    'display': '',
    'field_type': 'skip',
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'res_intro': {
    'display': '',
    'field_type': 'skip',
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'int_finalboss_movies': {
    'display': '',
    'field_type': 'skip',
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'unk_finalboss_movies': {
    'display': '',
    'field_type': 'skip',
    'offset': (offset_tmp:=offset_tmp+1),
    'length': 1,
  },
  'int_jungle_fishgame': {
    'display': '',
    'field_type': 'skip',
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

def WindowToggleLoading(window, showLoading: bool):
  if showLoading:
    window['loading'].update(visible=True)
    window['loading'].unhide_row()
    window['main'].update(visible=False)
    window['main'].hide_row()
  else:
    window['loading'].update(visible=False)
    window['loading'].hide_row()
    window['main'].update(visible=True)
    window['main'].unhide_row()

  window.refresh()

# parse LAYOUT from yaml file
LAYOUT = []
with open('layout.yaml', 'r') as layout_yaml:
  LAYOUT = yaml.load(layout_yaml, Loader=yaml.FullLoader)

# parse PREFS from yaml file
PREF = {
  'bg_color': '#000000',
  'label_font_color': 'white',
  'label_font_name': 'Arial',
  'label_font_size': 16,
  'counter_font_color': 'white',
  'counter_font_name': 'Arial',
  'counter_font_size': 36,
  'icon_shrink_factor': 1,
  'uncollected_transparency': 47
}
with open('prefs.yaml', 'r') as prefs_yaml:
  PREFS = yaml.load(prefs_yaml, Loader=yaml.FullLoader)

# reduce fields we lookup to those shown in layout
FIELDS_REDUCED = {}
for key in FIELDS:
  for row in LAYOUT:
    if key in row:
      FIELDS_REDUCED[key] = FIELDS[key]
      break

# setup window
PSG_LAYOUT = [
  [PSG.Text('Loading...', visible=True, key='loading', background_color=PREFS['bg_color'], font=(PREFS['counter_font_name'], PREFS['counter_font_size']), text_color=PREFS['counter_font_color'])]
]
tmp_rows = []
for row in LAYOUT:
  psg_row = []
  if row == "HSeparator":
    psg_row.append(PSG.HSeparator(key='HSeparator'))
  else:  
    for element in row:
      if element in FIELDS:
        field_info = FIELDS[element]
        if field_info['field_type'] == 'cell':
          # show icon for this cell
          img = Image.open('icons/' + field_info['icons'][0]).convert('RGBA')
          psg_row.append(PSG.Image(source=PilImageToBytesAlpha(img, PREFS['uncollected_transparency']), background_color=PREFS['bg_color'], subsample=PREFS['icon_shrink_factor'], key=element))
        elif field_info['field_type'] == 'counter':
          # show icon and counter
          psg_row.append(PSG.Image(source='icons/' + field_info['icons'][0], background_color=PREFS['bg_color'], subsample=PREFS['icon_shrink_factor'], key=element))
          psg_row.append(PSG.Text('0', size=(4,1), background_color=PREFS['bg_color'], font=(PREFS['counter_font_name'], PREFS['counter_font_size']), text_color=PREFS['counter_font_color'], key=element+'_counter'))
      elif element == 'completion_percent':
        # this is computed manually in tracker, so needs to be handled a bit differently
        psg_row.append(PSG.Text('0.0%', size=(4,1), background_color=PREFS['bg_color'], font=(PREFS['counter_font_name'], PREFS['counter_font_size']), text_color=PREFS['counter_font_color'], key=element))
      elif element[0] == '$':
        # $ first character indicates a text label
        if 'label_fixed_width' in PREFS:
          # fixed width
          psg_row.append(PSG.Text(element[1:], size=(PREFS['label_fixed_width'],1), background_color=PREFS['bg_color'], font=(PREFS['label_font_name'], PREFS['label_font_size']), text_color=PREFS['label_font_color'], key=element))
        else:
          # dynamic width
          psg_row.append(PSG.Text(element[1:], background_color=PREFS['bg_color'], font=(PREFS['label_font_name'], PREFS['label_font_size']), text_color=PREFS['label_font_color'], key=element))
      else:
        print(f'ERROR: invalid layout config for {element}')
  tmp_rows.append(psg_row)
PSG_LAYOUT.append([PSG.Column(tmp_rows, visible=False, background_color=PREFS['bg_color'], key='main')])

WINDOW = PSG.Window('OpenGOAL Tracker', PSG_LAYOUT, icon='appicon.ico', background_color=PREFS['bg_color'], finalize=True)
WINDOW.refresh()

OGAT = OpenGoalAutoTracker()

# display/refresh loop
while True:
  event, values = WINDOW.read(timeout=100) # only refresh up to 10x per sec
  if event == PSG.WIN_CLOSED:
    break

  match OGAT.status:
    case 'wakeup':
      # need to connect and find markers the first time
      WindowToggleLoading(WINDOW, True)
      OGAT.find_markers(True)
    case 'no_gk':
      # gk.exe not found, let user retry
      WindowToggleLoading(WINDOW, True)
      ans = PSG.popup_yes_no('Couldn''t find OpenGOAL process (gk.exe)! Try again?', icon='appicon.ico', title='Info', text_color=PREFS['label_font_color'], background_color=PREFS['bg_color'], keep_on_top=True)
      if ans == 'Yes':
        # this might still fail, will catch in next loop iteration
        OGAT.find_markers(True)
      else:
        break
    case 'connected':
      # connected but still looking for marker address, keep waiting
      WindowToggleLoading(WINDOW, True)
    case 'no_marker':
      # marker address not found, let user retry
      WindowToggleLoading(WINDOW, True)
      ans = PSG.popup_yes_no('Couldn''t successfully read OpenGOAL memory! Try again?', icon='appicon.ico', title='Info', text_color=PREFS['label_font_color'], background_color=PREFS['bg_color'], keep_on_top=True)
      if ans == 'Yes':
        # this might still fail, will catch in next loop iteration
        OGAT.find_markers(True)
      else:
        break
    case 'marker':
      # yay we can proceed
      WindowToggleLoading(WINDOW, False)

      values = OGAT.read_field_values(FIELDS_REDUCED)
      if values is not None:
        for key in values:
          if key in FIELDS_REDUCED:
            field_info = FIELDS_REDUCED[key]
            if field_info['field_type'] == 'cell':
              # show icon for this cell
              img = Image.open('icons/' + field_info['icons'][0]).convert('RGBA')
              if values[key] == 0:
                # use low opacity if not collected
                WINDOW[key].update(source=PilImageToBytesAlpha(img, PREFS['uncollected_transparency']), subsample=PREFS['icon_shrink_factor'])
              else:
                WINDOW[key].update(source=PilImageToBytesAlpha(img, 255), subsample=PREFS['icon_shrink_factor'])
            elif field_info['field_type'] == 'counter':
              # update counter value
              WINDOW[key+'_counter'].update(values[key])
            else:
              print(f'ERROR: unrecognized value returned from autotracker {key}')
          elif key == 'completion_percent':
            # this is computed manually in tracker, so needs to be handled a bit differently
            WINDOW[key].update(f'{values[key]:0.1f}%')

WINDOW.close()