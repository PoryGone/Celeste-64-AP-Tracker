import re
from typing import Dict, List


class LocationName:
    # Strawberry Locations
    strawberry_1  = "First Strawberry"
    strawberry_2  = "Floating Blocks Strawberry"
    strawberry_3  = "South-East Tower Top Strawberry"
    strawberry_4  = "Theo Strawberry"
    strawberry_5  = "Fall Through Spike Floor Strawberry"
    strawberry_6  = "Troll Strawberry"
    strawberry_7  = "Falling Blocks Strawberry"
    strawberry_8  = "Traffic Block Strawberry"
    strawberry_9  = "South-West Dash Refills Strawberry"
    strawberry_10 = "South-East Tower Side Strawberry"
    strawberry_11 = "Girders Strawberry"
    strawberry_12 = "North-East Tower Bottom Strawberry"
    strawberry_13 = "Breakable Blocks Strawberry"
    strawberry_14 = "Feather Maze Strawberry"
    strawberry_15 = "Feather Chain Strawberry"
    strawberry_16 = "Feather Hidden Strawberry"
    strawberry_17 = "Double Dash Puzzle Strawberry"
    strawberry_18 = "Double Dash Spike Climb Strawberry"
    strawberry_19 = "Double Dash Spring Strawberry"
    strawberry_20 = "North-East Tower Breakable Bottom Strawberry"
    strawberry_21 = "Theo Tower Lower Cassette Strawberry"
    strawberry_22 = "Theo Tower Upper Cassette Strawberry"
    strawberry_23 = "South End of Bridge Cassette Strawberry"
    strawberry_24 = "You Are Ready Cassette Strawberry"
    strawberry_25 = "Cassette Hidden in the House Strawberry"
    strawberry_26 = "North End of Bridge Cassette Strawberry"
    strawberry_27 = "Distant Feather Cassette Strawberry"
    strawberry_28 = "Feather Arches Cassette Strawberry"
    strawberry_29 = "North-East Tower Cassette Strawberry"
    strawberry_30 = "Badeline Cassette Strawberry"

    # Friend Locations
    granny_1   = "Granny Conversation 1"
    granny_2   = "Granny Conversation 2"
    granny_3   = "Granny Conversation 3"
    theo_1     = "Theo Conversation 1"
    theo_2     = "Theo Conversation 2"
    theo_3     = "Theo Conversation 3"
    badeline_1 = "Badeline Conversation 1"
    badeline_2 = "Badeline Conversation 2"
    badeline_3 = "Badeline Conversation 3"

    # Sign Locations
    sign_1 = "Camera Sign"
    sign_2 = "Skid Jump Sign"
    sign_3 = "Dash Jump Sign"
    sign_4 = "Lonely Sign"
    sign_5 = "Credits Sign"

    # Car Locations
    car_1 = "Intro Car"
    car_2 = "Secret Car"


class ItemName:
    strawberry = "Strawberry"
    raspberry = "Raspberry"

    dash_refill        = "Dash Refills"
    double_dash_refill = "Double Dash Refills"
    feather            = "Feathers"
    coin               = "Coins"
    cassette           = "Cassettes"

    traffic_block = "Traffic Blocks"
    spring        = "Springs"
    breakables    = "Breakable Blocks"

    ground_dash = "Ground Dash"
    air_dash    = "Air Dash"
    skid_jump   = "Skid Jump"
    climb       = "Climb"



location_standard_logic: Dict[str, List[List[str]]] = {
    LocationName.strawberry_4:  [[ItemName.traffic_block, ItemName.breakables]],
    LocationName.strawberry_6:  [[ItemName.dash_refill],
                                 [ItemName.traffic_block]],
    LocationName.strawberry_7:  [[ItemName.dash_refill],
                                 [ItemName.traffic_block]],
    LocationName.strawberry_8:  [[ItemName.traffic_block]],
    LocationName.strawberry_9:  [[ItemName.dash_refill]],
    LocationName.strawberry_11: [[ItemName.dash_refill],
                                 [ItemName.traffic_block]],
    LocationName.strawberry_12: [[ItemName.dash_refill, ItemName.double_dash_refill],
                                 [ItemName.traffic_block, ItemName.double_dash_refill]],
    LocationName.strawberry_13: [[ItemName.dash_refill, ItemName.breakables],
                                 [ItemName.traffic_block, ItemName.breakables]],
    LocationName.strawberry_14: [[ItemName.dash_refill, ItemName.feather],
                                 [ItemName.traffic_block, ItemName.feather]],
    LocationName.strawberry_15: [[ItemName.dash_refill, ItemName.feather],
                                 [ItemName.traffic_block, ItemName.feather]],
    LocationName.strawberry_16: [[ItemName.dash_refill, ItemName.feather],
                                 [ItemName.traffic_block, ItemName.feather]],
    LocationName.strawberry_17: [[ItemName.double_dash_refill, ItemName.feather, ItemName.traffic_block]],
    LocationName.strawberry_18: [[ItemName.dash_refill, ItemName.double_dash_refill],
                                 [ItemName.traffic_block, ItemName.feather, ItemName.double_dash_refill]],
    LocationName.strawberry_19: [[ItemName.dash_refill, ItemName.double_dash_refill, ItemName.spring],
                                 [ItemName.traffic_block, ItemName.double_dash_refill, ItemName.feather, ItemName.spring]],
    LocationName.strawberry_20: [[ItemName.dash_refill, ItemName.feather, ItemName.breakables],
                                 [ItemName.traffic_block, ItemName.feather, ItemName.breakables]],

    LocationName.strawberry_21: [[ItemName.cassette, ItemName.traffic_block, ItemName.breakables]],
    LocationName.strawberry_22: [[ItemName.cassette, ItemName.dash_refill, ItemName.breakables]],
    LocationName.strawberry_23: [[ItemName.cassette, ItemName.dash_refill, ItemName.coin],
                                 [ItemName.cassette, ItemName.traffic_block, ItemName.coin]],
    LocationName.strawberry_24: [[ItemName.cassette, ItemName.dash_refill, ItemName.traffic_block]],
    LocationName.strawberry_25: [[ItemName.cassette, ItemName.dash_refill, ItemName.double_dash_refill],
                                 [ItemName.cassette, ItemName.traffic_block, ItemName.feather, ItemName.double_dash_refill]],
    LocationName.strawberry_26: [[ItemName.cassette, ItemName.dash_refill],
                                 [ItemName.cassette, ItemName.traffic_block]],
    LocationName.strawberry_27: [[ItemName.cassette, ItemName.dash_refill, ItemName.feather, ItemName.coin],
                                 [ItemName.cassette, ItemName.traffic_block, ItemName.feather, ItemName.coin]],
    LocationName.strawberry_28: [[ItemName.cassette, ItemName.dash_refill, ItemName.feather, ItemName.coin],
                                 [ItemName.cassette, ItemName.traffic_block, ItemName.feather, ItemName.coin]],
    LocationName.strawberry_29: [[ItemName.cassette, ItemName.dash_refill, ItemName.feather, ItemName.coin]],
    LocationName.strawberry_30: [[ItemName.cassette, ItemName.dash_refill, ItemName.double_dash_refill, ItemName.feather, ItemName.traffic_block, ItemName.spring, ItemName.breakables]],

    LocationName.theo_1:     [[ItemName.traffic_block, ItemName.breakables]],
    LocationName.theo_2:     [[ItemName.traffic_block, ItemName.breakables]],
    LocationName.theo_3:     [[ItemName.traffic_block, ItemName.breakables]],
    LocationName.badeline_1: [[ItemName.double_dash_refill, ItemName.feather, ItemName.traffic_block, ItemName.breakables]],
    LocationName.badeline_2: [[ItemName.double_dash_refill, ItemName.feather, ItemName.traffic_block, ItemName.breakables]],
    LocationName.badeline_3: [[ItemName.double_dash_refill, ItemName.feather, ItemName.traffic_block, ItemName.breakables]],

    LocationName.sign_2: [[ItemName.breakables]],
    LocationName.sign_3: [[ItemName.dash_refill],
                          [ItemName.traffic_block]],
    LocationName.sign_4: [[ItemName.dash_refill, ItemName.double_dash_refill],
                          [ItemName.dash_refill, ItemName.feather],
                          [ItemName.traffic_block, ItemName.feather]],
    LocationName.sign_5: [[ItemName.double_dash_refill, ItemName.feather, ItemName.traffic_block, ItemName.breakables]],

    LocationName.car_2: [[ItemName.breakables]],
}

location_hard_logic: Dict[str, List[List[str]]] = {
    LocationName.strawberry_13: [[ItemName.breakables]],
    LocationName.strawberry_17: [[ItemName.double_dash_refill, ItemName.traffic_block]],
    LocationName.strawberry_20: [[ItemName.breakables]],

    LocationName.strawberry_21: [[ItemName.cassette, ItemName.traffic_block, ItemName.breakables]],
    LocationName.strawberry_22: [[ItemName.cassette]],
    LocationName.strawberry_23: [[ItemName.cassette, ItemName.coin]],
    LocationName.strawberry_24: [[ItemName.cassette]],
    LocationName.strawberry_25: [[ItemName.cassette, ItemName.double_dash_refill]],
    LocationName.strawberry_26: [[ItemName.cassette]],
    LocationName.strawberry_27: [[ItemName.cassette]],
    LocationName.strawberry_28: [[ItemName.cassette, ItemName.feather]],
    LocationName.strawberry_29: [[ItemName.cassette]],
    LocationName.strawberry_30: [[ItemName.cassette, ItemName.dash_refill, ItemName.double_dash_refill, ItemName.traffic_block, ItemName.breakables]],

    LocationName.sign_2: [[ItemName.breakables]],

    LocationName.car_2: [[ItemName.breakables]],
}

location_standard_moves_logic: Dict[str, List[List[str]]] = {
    LocationName.strawberry_1:  [[ItemName.ground_dash],
                                 [ItemName.air_dash],
                                 [ItemName.skid_jump],
                                 [ItemName.climb]],
    LocationName.strawberry_2:  [[ItemName.ground_dash],
                                 [ItemName.air_dash],
                                 [ItemName.skid_jump],
                                 [ItemName.climb]],
    LocationName.strawberry_3:  [[ItemName.air_dash],
                                 [ItemName.skid_jump]],
    LocationName.strawberry_4:  [[ItemName.traffic_block, ItemName.breakables, ItemName.air_dash]],
    LocationName.strawberry_5:  [[ItemName.air_dash]],
    LocationName.strawberry_6:  [[ItemName.dash_refill, ItemName.air_dash],
                                 [ItemName.traffic_block, ItemName.ground_dash],
                                 [ItemName.traffic_block, ItemName.air_dash],
                                 [ItemName.traffic_block, ItemName.skid_jump],
                                 [ItemName.traffic_block, ItemName.climb]],
    LocationName.strawberry_7:  [[ItemName.dash_refill, ItemName.air_dash],
                                 [ItemName.traffic_block, ItemName.ground_dash],
                                 [ItemName.traffic_block, ItemName.air_dash],
                                 [ItemName.traffic_block, ItemName.skid_jump],
                                 [ItemName.traffic_block, ItemName.climb]],
    LocationName.strawberry_8:  [[ItemName.traffic_block, ItemName.ground_dash],
                                 [ItemName.traffic_block, ItemName.air_dash],
                                 [ItemName.traffic_block, ItemName.skid_jump],
                                 [ItemName.traffic_block, ItemName.climb]],
    LocationName.strawberry_9:  [[ItemName.dash_refill, ItemName.air_dash]],
    LocationName.strawberry_10: [[ItemName.climb]],
    LocationName.strawberry_11: [[ItemName.dash_refill, ItemName.air_dash, ItemName.climb],
                                 [ItemName.traffic_block, ItemName.climb]],
    LocationName.strawberry_12: [[ItemName.dash_refill, ItemName.double_dash_refill, ItemName.air_dash],
                                 [ItemName.traffic_block, ItemName.double_dash_refill, ItemName.air_dash]],
    LocationName.strawberry_13: [[ItemName.dash_refill, ItemName.breakables, ItemName.air_dash],
                                 [ItemName.traffic_block, ItemName.breakables, ItemName.ground_dash],
                                 [ItemName.traffic_block, ItemName.breakables, ItemName.air_dash]],
    LocationName.strawberry_14: [[ItemName.dash_refill, ItemName.feather, ItemName.air_dash],
                                 [ItemName.traffic_block, ItemName.feather, ItemName.air_dash]],
    LocationName.strawberry_15: [[ItemName.dash_refill, ItemName.feather, ItemName.air_dash, ItemName.climb],
                                 [ItemName.traffic_block, ItemName.feather, ItemName.climb]],
    LocationName.strawberry_16: [[ItemName.dash_refill, ItemName.feather, ItemName.air_dash],
                                 [ItemName.traffic_block, ItemName.feather]],
    LocationName.strawberry_17: [[ItemName.double_dash_refill, ItemName.feather, ItemName.traffic_block, ItemName.ground_dash],
                                 [ItemName.double_dash_refill, ItemName.feather, ItemName.traffic_block, ItemName.air_dash],
                                 [ItemName.double_dash_refill, ItemName.feather, ItemName.traffic_block, ItemName.skid_jump],
                                 [ItemName.double_dash_refill, ItemName.feather, ItemName.traffic_block, ItemName.climb]],
    LocationName.strawberry_18: [[ItemName.dash_refill, ItemName.double_dash_refill, ItemName.air_dash, ItemName.climb],
                                 [ItemName.traffic_block, ItemName.feather, ItemName.double_dash_refill, ItemName.air_dash, ItemName.climb]],
    LocationName.strawberry_19: [[ItemName.dash_refill, ItemName.double_dash_refill, ItemName.spring, ItemName.air_dash],
                                 [ItemName.traffic_block, ItemName.double_dash_refill, ItemName.feather, ItemName.spring, ItemName.air_dash]],
    LocationName.strawberry_20: [[ItemName.dash_refill, ItemName.feather, ItemName.breakables, ItemName.air_dash],
                                 [ItemName.traffic_block, ItemName.feather, ItemName.breakables, ItemName.air_dash]],

    LocationName.strawberry_21: [[ItemName.cassette, ItemName.traffic_block, ItemName.breakables, ItemName.air_dash]],
    LocationName.strawberry_22: [[ItemName.cassette, ItemName.dash_refill, ItemName.breakables, ItemName.air_dash]],
    LocationName.strawberry_23: [[ItemName.cassette, ItemName.dash_refill, ItemName.coin, ItemName.air_dash, ItemName.climb],
                                 [ItemName.cassette, ItemName.traffic_block, ItemName.coin, ItemName.air_dash, ItemName.climb]],
    LocationName.strawberry_24: [[ItemName.cassette, ItemName.dash_refill, ItemName.traffic_block, ItemName.air_dash]],
    LocationName.strawberry_25: [[ItemName.cassette, ItemName.dash_refill, ItemName.double_dash_refill, ItemName.air_dash, ItemName.climb],
                                 [ItemName.cassette, ItemName.traffic_block, ItemName.feather, ItemName.double_dash_refill, ItemName.air_dash, ItemName.climb]],
    LocationName.strawberry_26: [[ItemName.cassette, ItemName.dash_refill, ItemName.air_dash, ItemName.climb],
                                 [ItemName.cassette, ItemName.traffic_block, ItemName.air_dash, ItemName.climb]],
    LocationName.strawberry_27: [[ItemName.cassette, ItemName.dash_refill, ItemName.feather, ItemName.coin, ItemName.air_dash],
                                 [ItemName.cassette, ItemName.traffic_block, ItemName.feather, ItemName.coin, ItemName.air_dash]],
    LocationName.strawberry_28: [[ItemName.cassette, ItemName.dash_refill, ItemName.feather, ItemName.coin, ItemName.air_dash, ItemName.climb],
                                 [ItemName.cassette, ItemName.traffic_block, ItemName.feather, ItemName.coin, ItemName.air_dash, ItemName.climb]],
    LocationName.strawberry_29: [[ItemName.cassette, ItemName.dash_refill, ItemName.feather, ItemName.coin, ItemName.air_dash, ItemName.skid_jump]],
    LocationName.strawberry_30: [[ItemName.cassette, ItemName.dash_refill, ItemName.double_dash_refill, ItemName.feather, ItemName.traffic_block, ItemName.spring, ItemName.breakables, ItemName.air_dash, ItemName.climb]],

    LocationName.granny_1:   [[ItemName.ground_dash],
                              [ItemName.air_dash],
                              [ItemName.skid_jump],
                              [ItemName.climb]],
    LocationName.granny_2:   [[ItemName.ground_dash],
                              [ItemName.air_dash],
                              [ItemName.skid_jump],
                              [ItemName.climb]],
    LocationName.granny_3:   [[ItemName.ground_dash],
                              [ItemName.air_dash],
                              [ItemName.skid_jump],
                              [ItemName.climb]],
    LocationName.theo_1:     [[ItemName.traffic_block, ItemName.breakables, ItemName.air_dash]],
    LocationName.theo_2:     [[ItemName.traffic_block, ItemName.breakables, ItemName.air_dash]],
    LocationName.theo_3:     [[ItemName.traffic_block, ItemName.breakables, ItemName.air_dash]],
    LocationName.badeline_1: [[ItemName.double_dash_refill, ItemName.feather, ItemName.traffic_block, ItemName.breakables, ItemName.air_dash, ItemName.climb]],
    LocationName.badeline_2: [[ItemName.double_dash_refill, ItemName.feather, ItemName.traffic_block, ItemName.breakables, ItemName.air_dash, ItemName.climb]],
    LocationName.badeline_3: [[ItemName.double_dash_refill, ItemName.feather, ItemName.traffic_block, ItemName.breakables, ItemName.air_dash, ItemName.climb]],

    LocationName.sign_1: [[ItemName.ground_dash],
                          [ItemName.air_dash],
                          [ItemName.skid_jump],
                          [ItemName.climb]],
    LocationName.sign_2: [[ItemName.breakables, ItemName.ground_dash],
                          [ItemName.breakables, ItemName.air_dash]],
    LocationName.sign_3:  [[ItemName.dash_refill, ItemName.air_dash],
                           [ItemName.traffic_block, ItemName.ground_dash],
                           [ItemName.traffic_block, ItemName.air_dash],
                           [ItemName.traffic_block, ItemName.skid_jump],
                           [ItemName.traffic_block, ItemName.climb]],
    LocationName.sign_4: [[ItemName.dash_refill, ItemName.double_dash_refill, ItemName.air_dash],
                          [ItemName.dash_refill, ItemName.feather, ItemName.air_dash],
                          [ItemName.traffic_block, ItemName.feather, ItemName.ground_dash],
                          [ItemName.traffic_block, ItemName.feather, ItemName.air_dash],
                          [ItemName.traffic_block, ItemName.feather, ItemName.skid_jump],
                          [ItemName.traffic_block, ItemName.feather, ItemName.climb]],
    LocationName.sign_5: [[ItemName.double_dash_refill, ItemName.feather, ItemName.traffic_block, ItemName.breakables, ItemName.air_dash, ItemName.climb]],

    LocationName.car_2: [[ItemName.breakables, ItemName.ground_dash],
                         [ItemName.breakables, ItemName.air_dash]],
}

location_hard_moves_logic: Dict[str, List[List[str]]] = {
    LocationName.strawberry_3:  [[ItemName.air_dash],
                                 [ItemName.skid_jump]],
    LocationName.strawberry_5:  [[ItemName.ground_dash],
                                 [ItemName.air_dash]],
    LocationName.strawberry_8:  [[ItemName.traffic_block],
                                 [ItemName.ground_dash, ItemName.air_dash]],
    LocationName.strawberry_10: [[ItemName.air_dash],
                                 [ItemName.climb]],
    LocationName.strawberry_11: [[ItemName.ground_dash],
                                 [ItemName.air_dash],
                                 [ItemName.skid_jump]],
    LocationName.strawberry_12: [[ItemName.feather],
                                 [ItemName.ground_dash],
                                 [ItemName.air_dash]],
    LocationName.strawberry_13: [[ItemName.breakables, ItemName.ground_dash],
                                 [ItemName.breakables, ItemName.air_dash]],
    LocationName.strawberry_14: [[ItemName.feather, ItemName.air_dash],
                                 [ItemName.air_dash, ItemName.climb]],
    LocationName.strawberry_15: [[ItemName.feather],
                                 [ItemName.ground_dash, ItemName.air_dash]],
    LocationName.strawberry_17: [[ItemName.double_dash_refill, ItemName.traffic_block]],
    LocationName.strawberry_18: [[ItemName.air_dash, ItemName.climb],
                                 [ItemName.double_dash_refill, ItemName.air_dash]],
    LocationName.strawberry_19: [[ItemName.air_dash, ItemName.skid_jump],
                                 [ItemName.double_dash_refill, ItemName.spring, ItemName.air_dash],
                                 [ItemName.spring, ItemName.ground_dash, ItemName.air_dash]],
    LocationName.strawberry_20: [[ItemName.breakables, ItemName.air_dash]],

    LocationName.strawberry_21: [[ItemName.cassette, ItemName.traffic_block, ItemName.breakables, ItemName.air_dash]],
    LocationName.strawberry_22: [[ItemName.cassette, ItemName.ground_dash, ItemName.air_dash],
                                 [ItemName.cassette, ItemName.dash_refill, ItemName.air_dash]],
    LocationName.strawberry_23: [[ItemName.cassette, ItemName.coin, ItemName.air_dash]],
    LocationName.strawberry_24: [[ItemName.cassette, ItemName.ground_dash, ItemName.air_dash],
                                 [ItemName.cassette, ItemName.traffic_block, ItemName.air_dash]],
    LocationName.strawberry_25: [[ItemName.cassette, ItemName.double_dash_refill, ItemName.air_dash, ItemName.climb]],
    LocationName.strawberry_26: [[ItemName.cassette, ItemName.ground_dash],
                                 [ItemName.cassette, ItemName.air_dash]],
    LocationName.strawberry_27: [[ItemName.cassette, ItemName.air_dash, ItemName.skid_jump],
                                 [ItemName.cassette, ItemName.traffic_block, ItemName.coin, ItemName.air_dash],
                                 [ItemName.cassette, ItemName.coin, ItemName.ground_dash],
                                 [ItemName.cassette, ItemName.feather, ItemName.coin, ItemName.air_dash]],
    LocationName.strawberry_28: [[ItemName.cassette, ItemName.feather, ItemName.air_dash],
                                 [ItemName.cassette, ItemName.feather, ItemName.climb]],
    LocationName.strawberry_29: [[ItemName.cassette, ItemName.dash_refill, ItemName.air_dash, ItemName.skid_jump],
                                 [ItemName.cassette, ItemName.ground_dash, ItemName.air_dash]],
    LocationName.strawberry_30: [[ItemName.cassette, ItemName.dash_refill, ItemName.double_dash_refill, ItemName.traffic_block, ItemName.breakables, ItemName.ground_dash, ItemName.air_dash, ItemName.climb, ItemName.skid_jump],
                                 [ItemName.cassette, ItemName.dash_refill, ItemName.double_dash_refill, ItemName.traffic_block, ItemName.breakables, ItemName.feather, ItemName.air_dash, ItemName.climb, ItemName.skid_jump],
                                 [ItemName.cassette, ItemName.dash_refill, ItemName.double_dash_refill, ItemName.traffic_block, ItemName.breakables, ItemName.spring, ItemName.ground_dash, ItemName.air_dash, ItemName.climb],
                                 [ItemName.cassette, ItemName.dash_refill, ItemName.double_dash_refill, ItemName.traffic_block, ItemName.breakables, ItemName.spring, ItemName.feather, ItemName.air_dash, ItemName.climb]],

    LocationName.badeline_1: [[ItemName.double_dash_refill, ItemName.feather, ItemName.traffic_block, ItemName.breakables, ItemName.air_dash, ItemName.climb],
                              [ItemName.traffic_block, ItemName.air_dash, ItemName.skid_jump],
                              [ItemName.ground_dash, ItemName.air_dash, ItemName.skid_jump],
                              [ItemName.feather, ItemName.traffic_block, ItemName.air_dash],
                              [ItemName.traffic_block, ItemName.ground_dash, ItemName.air_dash]],
    LocationName.badeline_2: [[ItemName.double_dash_refill, ItemName.feather, ItemName.traffic_block, ItemName.breakables, ItemName.air_dash, ItemName.climb],
                              [ItemName.traffic_block, ItemName.air_dash, ItemName.skid_jump],
                              [ItemName.ground_dash, ItemName.air_dash, ItemName.skid_jump],
                              [ItemName.feather, ItemName.traffic_block, ItemName.air_dash],
                              [ItemName.traffic_block, ItemName.ground_dash, ItemName.air_dash]],
    LocationName.badeline_3: [[ItemName.double_dash_refill, ItemName.feather, ItemName.traffic_block, ItemName.breakables, ItemName.air_dash, ItemName.climb],
                              [ItemName.traffic_block, ItemName.air_dash, ItemName.skid_jump],
                              [ItemName.ground_dash, ItemName.air_dash, ItemName.skid_jump],
                              [ItemName.feather, ItemName.traffic_block, ItemName.air_dash],
                              [ItemName.traffic_block, ItemName.ground_dash, ItemName.air_dash]],

    LocationName.sign_2: [[ItemName.breakables, ItemName.ground_dash],
                          [ItemName.breakables, ItemName.air_dash]],
    LocationName.sign_5: [[ItemName.double_dash_refill, ItemName.feather, ItemName.traffic_block, ItemName.breakables, ItemName.air_dash, ItemName.climb],
                          [ItemName.traffic_block, ItemName.air_dash, ItemName.skid_jump],
                          [ItemName.ground_dash, ItemName.air_dash, ItemName.skid_jump],
                          [ItemName.feather, ItemName.traffic_block, ItemName.air_dash],
                          [ItemName.traffic_block, ItemName.ground_dash, ItemName.air_dash]],

    LocationName.car_2: [[ItemName.breakables, ItemName.ground_dash],
                         [ItemName.breakables, ItemName.air_dash]],
}


def dump_lua(data):
    if type(data) is str:
        return f'"{re.escape(data)}"'
    if type(data) in (int, float):
        return f'{data}'
    if type(data) is bool:
        return data and "true" or "false"
    if type(data) is list:
        l = "{"
        l += ", ".join([dump_lua(item) for item in data])
        l += "}"
        return l
    if type(data) is dict:
        t = "{"
        t += ", ".join([f'[\"{re.escape(k)}\"]={dump_lua(v)}' for k,v in data.items()])
        t += "}"
        return t




with open("out_data.lua", "w") as out_file:
    out_file.write("\n")
    out_file.write("\n")
    out_file.write(f"location_standard_logic = ")
    out_file.write(dump_lua(location_standard_logic))
    out_file.write("\n")
    out_file.write("\n")
    out_file.write(f"location_hard_logic = ")
    out_file.write(dump_lua(location_hard_logic))
    out_file.write("\n")
    out_file.write("\n")
    out_file.write(f"location_standard_moves_logic = ")
    out_file.write(dump_lua(location_standard_moves_logic))
    out_file.write("\n")
    out_file.write("\n")
    out_file.write(f"location_hard_moves_logic = ")
    out_file.write(dump_lua(location_hard_moves_logic))
    out_file.write("\n")
    out_file.write("\n")
