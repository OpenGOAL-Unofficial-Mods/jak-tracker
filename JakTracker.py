from OpenGoalAutoTracker import OpenGoalAutoTracker

# config for fields to query
offset_tmp = 0
FIELDS = {
  "num_power_cells": {
    "display": "POWER CELLS",
    "icon_type": "counter",
    "icons": [
      "cell_counter.png",
    ],
    "offset": offset_tmp,
    "length": 4,
  },
  "num_orbs": {
    "display": "PRECURSOR ORBS (TOTAL)",
    "icon_type": "counter",
    "icons": [
      "orb_counter.png",
    ],
    "offset": (offset_tmp:=offset_tmp+4),
    "length": 4,
  },
  "num_scout_flies": {
    "display": "SCOUT FLIES (TOTAL)",
    "icon_type": "counter",
    "icons": [
      "fly_counter.png",
    ],
    "offset": (offset_tmp:=offset_tmp+4),
    "length": 4,
  },
  "padding_stats": {
    "display": "padding_stats",
    "icon_type": "skip",
    "offset": (offset_tmp:=offset_tmp+4),
    "length": 200,
  },
  "game_hash": {
    "display": "game_hash",
    "icon_type": "skip",
    "offset": (offset_tmp:=offset_tmp+200), # 212
    "length": 4,
  },
  "in_cutscene": {
    "display": "in_cutscene",
    "icon_type": "skip",
    "offset": (offset_tmp:=offset_tmp+4),
    "length": 4,
  },
  "is_loading": {
    "display": "is_loading",
    "icon_type": "skip",
    "offset": (offset_tmp:=offset_tmp+4),
    "length": 4,
  },
  "padding_controls": {
    "display": "padding_controls",
    "icon_type": "skip",
    "offset": (offset_tmp:=offset_tmp+4),
    "length": 200,
  },
  "res_training_gimmie": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+200), # 424
    "length": 1,
  },
  "res_training_door": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_training_climb": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_training_buzzer": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_jungle_eggtop": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_jungle_lurkerm": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_jungle_tower": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_jungle_fishgame": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_jungle_plant": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_jungle_buzzer": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_jungle_canyon_end": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_jungle_temple_door": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_village1_yakow": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_village1_mayor_money": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_village1_uncle_money": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_village1_oracle_money1": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_village1_oracle_money2": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_village1_buzzer": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_beach_ecorocks": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_beach_pelican": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_beach_flutflut": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_beach_seagull": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_beach_cannon": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_beach_buzzer": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_beach_gimmie": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_beach_sentinel": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_misty_muse": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_misty_boat": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_misty_warehouse": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_misty_cannon": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_misty_bike": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_misty_buzzer": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_misty_bike_jump": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_misty_eco_challenge": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_village2_gambler_money": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_village2_geologist_money": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_village2_warrior_money": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_village2_oracle_money1": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_village2_oracle_money2": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_village2_buzzer": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_swamp_billy": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_swamp_flutflut": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_swamp_battle": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_swamp_tether_1": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_swamp_tether_2": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_swamp_tether_3": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_swamp_tether_4": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_swamp_buzzer": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_swamp_arm": {
    "display": "GET TO THE CENTER OF THE SWAMP",  # ayo?
    "icon_type": "skip",
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_sunken_platforms": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_sunken_pipe": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_sunken_slide": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_sunken_room": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_sunken_sharks": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_sunken_buzzer": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_sunken_top_of_helix": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_sunken_spinning_room": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_rolling_race": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_rolling_robbers": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_rolling_moles": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_rolling_plants": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_rolling_lake": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_rolling_buzzer": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_rolling_ring_chase_1": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_rolling_ring_chase_2": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_snow_eggtop": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_snow_ram": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_snow_fort": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_snow_ball": {
    "display": "OPEN THE LURKER FORT GATE",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_snow_bunnies": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_snow_buzzer": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_snow_bumpers": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_snow_cage": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_red_eggtop": {
    "display": "",
    "icon_type": "skip",
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_firecanyon_buzzer": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_firecanyon_end": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_citadel_sage_green": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_citadel_sage_blue": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_citadel_sage_red": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_citadel_sage_yellow": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_citadel_buzzer": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_village3_extra1": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_village3_buzzer": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_village3_miner_money1": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_village3_miner_money2": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_village3_miner_money3": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_village3_miner_money4": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_village3_oracle_money1": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_village3_oracle_money2": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_cave_gnawers": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_cave_dark_crystals": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_cave_dark_climb": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_cave_robot_climb": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_cave_swing_poles": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_cave_spider_tunnel": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_cave_platforms": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_cave_buzzer": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_ogre_boss": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_ogre_end": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_ogre_buzzer": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_ogre_secret": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_lavatube_end": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_lavatube_buzzer": {
    "display": "",
    "icon_type": "cell",
    "icons": [
      ".png",
    ],
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_lavatube_balls": {
    "display": "",
    "icon_type": "skip",
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "res_intro": {
    "display": "",
    "icon_type": "skip",
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "int_finalboss_movies": {
    "display": "",
    "icon_type": "skip",
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "unk_finalboss_movies": {
    "display": "",
    "icon_type": "skip",
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  },
  "int_jungle_fishgame": {
    "display": "",
    "icon_type": "skip",
    "offset": (offset_tmp:=offset_tmp+1),
    "length": 1,
  }
}

ogat = OpenGoalAutoTracker()
print(ogat.read_field_values(FIELDS))