
location_standard_moves_logic = {
    ["First Strawberry"] = {{"Ground Dash"}, {"Air Dash"}, {"Climb"}},
    ["Floating Blocks Strawberry"] = {{"Air Dash"}, {"Skid Jump"}},
    ["South-East Tower Top Strawberry"] = {{"Air Dash"}, {"Skid Jump"}},
    ["Theo Strawberry"] = {{"Traffic Blocks", "Breakable Blocks", "Air Dash"}},
    ["Fall Through Spike Floor Strawberry"] = {{"Air Dash"}},
    ["South-West Dash Refills Strawberry"] = {{"Dash Refills", "Air Dash"}},
    ["South-East Tower Side Strawberry"] = {{"Climb"}},
    ["Girders Strawberry"] = {{"Air Dash", "Climb"}},
    ["Breakable Blocks Strawberry"] = {{"Breakable Blocks", "Air Dash"}, {"Breakable Blocks", "Ground Dash"}},
    ["Feather Maze Strawberry"] = {{"Feathers", "Air Dash"}},
    ["Feather Chain Strawberry"] = {{"Feathers", "Air Dash", "Climb"}},
    ["Feather Hidden Strawberry"] = {{"Feathers"}},
    ["Double Dash Puzzle Strawberry"] = {{"Double Dash Refills", "Feathers", "Traffic Blocks"}},
    ["Double Dash Spike Climb Strawberry"] = {{"Double Dash Refills", "Air Dash", "Climb"}},
    ["Double Dash Spring Strawberry"] = {{"Double Dash Refills", "Springs", "Air Dash", "Skid Jump"}},
    ["Badeline Tower Breakable Bottom Strawberry"] = {{"Feathers", "Breakable Blocks", "Air Dash"}},

    ["Theo Tower Lower Cassette Strawberry"] = {{"Cassettes", "Traffic Blocks", "Breakable Blocks", "Air Dash"}},
    ["Theo Tower Upper Cassette Strawberry"] = {{"Cassettes", "Dash Refills", "Breakable Blocks", "Air Dash"}},
    ["South End of Bridge Cassette Strawberry"] = {{"Cassettes", "Coins", "Air Dash", "Climb"}},
    ["You Are Ready Cassette Strawberry"] = {{"Cassettes", "Dash Refills", "Traffic Blocks", "Air Dash"}},
    ["Cassette Hidden in the House Strawberry"] = {{"Cassettes", "Double Dash Refills", "Air Dash", "Climb"}},
    ["North End of Bridge Cassette Strawberry"] = {{"Cassettes", "Air Dash", "Climb"}},
    ["Distant Feather Cassette Strawberry"] = {{"Cassettes", "Feathers", "Coins", "Air Dash", "Climb"}},
    ["Feather Arches Cassette Strawberry"] = {{"Cassettes", "Feathers", "Coins", "Air Dash", "Climb"}},
    ["Badeline Tower Cassette Strawberry"] = {{"Cassettes", "Dash Refills", "Coins", "Air Dash", "Skid Jump"}},
    ["Badeline Cassette Strawberry"] = {{"Cassettes", "Dash Refills", "Double Dash Refills", "Feathers", "Traffic Blocks", "Springs", "Breakable Blocks", "Air Dash", "Climb"}},

    ["Theo Conversation 1"] = {{"Traffic Blocks", "Breakable Blocks", "Air Dash"}},
    ["Theo Conversation 2"] = {{"Traffic Blocks", "Breakable Blocks", "Air Dash"}},
    ["Theo Conversation 3"] = {{"Traffic Blocks", "Breakable Blocks", "Air Dash"}},

    ["Skid Jump Sign"] = {{"Breakable Blocks", "Ground Dash"}, {"Breakable Blocks", "Air Dash"}},

    ["Secret Car"] = {{"Breakable Blocks", "Ground Dash", "Climb"}, {"Breakable Blocks", "Air Dash", "Climb"}},


    -- Region Connection Rules
    ["Intro to Intro"] = {{"Intro Checkpoint"}},
    ["Intro to Granny"] = {{"Ground Dash"}, {"Air Dash"}, {"Skid Jump"}, {"Climb"}},

    ["Granny to Granny"] = {{"Granny Checkpoint"}, {"South-East Tower Checkpoint"}, {"Climb Sign Checkpoint"}},
    ["Granny to Freeway"] = {{"Air Dash", "Dash Refills"}},
    ["Granny to North-West Girders"] = {{"Traffic Blocks"}},
    ["Granny to South-East House"] = {{"Air Dash", "Climb", "Double Dash Refills"}},
    ["Granny to Badeline Tower Lower"] = {{"Air Dash", "Climb", "Dash Refills"}},

    ["Freeway to Granny"] = {{"Traffic Blocks"}, {"Air Dash", "Dash Refills"}},
    ["Freeway to Freeway"] = {{"Freeway Checkpoint"}, {"Freeway Feather Checkpoint"}},
    ["Freeway to North-West Girders"] = {{"Cannot Access"}},
    ["Freeway to North-East Feathers"] = {{"Feathers"}},

    ["North-West Girders to Freeway"] = {{"Traffic Blocks"}},

    ["North-East Feathers to Freeway"] = {{"Feathers"}},
    ["North-East Feathers to North-East Feathers"] = {{"Feather Maze Checkpoint"}},
    ["North-East Feathers to Badeline Tower Lower"] = {{"Feathers"}},
    ["North-East Feathers to Badeline Tower Upper"] = {{"Air Dash", "Climb", "Feathers"}},

    ["South-East House to Granny"] = {{"Air Dash", "Traffic Blocks", "Double Dash Refills"}},
    ["South-East House to South-East House"] = {{"Double Dash House Checkpoint"}},
    ["South-East House to Badeline Tower Lower"] = {{"Air Dash", "Double Dash Refills"}},

    ["Badeline Tower Lower to Granny"] = {{"Cannot Access"}},
    ["Badeline Tower Lower to North-East Feathers"] = {{"Air Dash", "Breakable Blocks", "Feathers"}},
    ["Badeline Tower Lower to South-East House"] = {{"Cannot Access"}},
    ["Badeline Tower Lower to Badeline Tower Upper"] = {{"Cannot Access"}},

    ["Badeline Tower Upper to Granny"] = {{"Dash Refills"}},
    ["Badeline Tower Upper to North-East Feathers"] = {{"Air Dash"}, {"Ground Dash"}},
    ["Badeline Tower Upper to South-East House"] = {{"Air Dash"}, {"Ground Dash"}},
    ["Badeline Tower Upper to Badeline Tower Upper"] = {{"Badeline Tower Checkpoint"}},
    ["Badeline Tower Upper to Badeline Island"] = {{"Air Dash", "Climb", "Traffic Blocks", "Double Dash Refills", "Breakable Blocks", "Feathers"}},

    ["Badeline Island to Badeline Tower Upper"] = {{"Air Dash"}, {"Ground Dash"}},
    ["Badeline Island to Badeline Island"] = {{"Badeline Island Checkpoint"}},
}


location_hard_moves_logic = {
    ["Fall Through Spike Floor Strawberry"] = {{"Ground Dash"}, {"Air Dash"}},
    ["South-East Tower Side Strawberry"] = {{"Air Dash"}, {"Climb"}},
    ["Girders Strawberry"] = {{"Ground Dash"}, {"Air Dash"}, {"Skid Jump"}},
    ["Breakable Blocks Strawberry"] = {{"Breakable Blocks", "Ground Dash"}, {"Breakable Blocks", "Air Dash"}},
    ["Feather Maze Strawberry"] = {{"Feathers", "Air Dash"}, {"Air Dash", "Climb"}, {"Double Dash Refills", "Air Dash"}},
    ["Feather Chain Strawberry"] = {{"Feathers"}, {"Ground Dash", "Air Dash"}},
    ["Double Dash Puzzle Strawberry"] = {{"Double Dash Refills", "Traffic Blocks"}},
    ["Double Dash Spike Climb Strawberry"] = {{"Air Dash", "Climb"}, {"Double Dash Refills", "Air Dash"}},
    ["Double Dash Spring Strawberry"] = {{"Air Dash", "Skid Jump"}, {"Double Dash Refills", "Springs", "Air Dash"}, {"Springs", "Ground Dash", "Air Dash"}},
    ["Badeline Tower Breakable Bottom Strawberry"] = {{"Breakable Blocks", "Air Dash"}},

    ["Theo Tower Lower Cassette Strawberry"] = {{"Cassettes", "Traffic Blocks", "Breakable Blocks", "Air Dash"}},
    ["Theo Tower Upper Cassette Strawberry"] = {{"Cassettes", "Ground Dash", "Air Dash"}, {"Cassettes", "Dash Refills", "Air Dash"}},
    ["South End of Bridge Cassette Strawberry"] = {{"Cassettes", "Coins", "Air Dash"}},
    ["You Are Ready Cassette Strawberry"] = {{"Cassettes", "Ground Dash", "Air Dash"}, {"Cassettes", "Traffic Blocks", "Air Dash"}},
    ["Cassette Hidden in the House Strawberry"] = {{"Cassettes", "Double Dash Refills", "Air Dash", "Climb"}},
    ["North End of Bridge Cassette Strawberry"] = {{"Cassettes", "Ground Dash"}, {"Cassettes", "Air Dash"}},
    ["Distant Feather Cassette Strawberry"] = {{"Cassettes", "Air Dash", "Skid Jump"}, {"Cassettes", "Traffic Blocks", "Coins", "Air Dash"}, {"Cassettes", "Coins", "Ground Dash"}, {"Cassettes", "Feathers", "Coins", "Air Dash"}},
    ["Feather Arches Cassette Strawberry"] = {{"Cassettes", "Feathers", "Air Dash"}, {"Cassettes", "Feathers", "Climb"}},
    ["Badeline Tower Cassette Strawberry"] = {{"Cassettes", "Dash Refills", "Air Dash", "Skid Jump"}, {"Cassettes", "Ground Dash", "Air Dash"}},
    ["Badeline Cassette Strawberry"] = {{"Cassettes", "Dash Refills", "Double Dash Refills", "Traffic Blocks", "Breakable Blocks", "Air Dash", "Climb", "Skid Jump"}, {"Cassettes", "Dash Refills", "Double Dash Refills", "Traffic Blocks", "Breakable Blocks", "Springs", "Air Dash", "Climb"}},

    ["Skid Jump Sign"] = {{"Breakable Blocks", "Ground Dash"}, {"Breakable Blocks", "Air Dash"}},

    ["Secret Car"] = {{"Breakable Blocks", "Ground Dash"}, {"Breakable Blocks", "Air Dash"}},


    -- Region Connection Rules
    ["Intro to Intro"] = {{"Intro Checkpoint"}},

    ["Granny to Granny"] = {{"Granny Checkpoint"}, {"South-East Tower Checkpoint"}, {"Climb Sign Checkpoint"}},
    ["Granny to North-West Girders"] = {{"Traffic Blocks"}},
    ["Granny to South-East House"] = {{"Air Dash", "Double Dash Refills"}, {"Ground Dash"}},
    ["Granny to Badeline Tower Lower"] = {{"Air Dash"}, {"Ground Dash"}},

    ["Freeway to Freeway"] = {{"Freeway Checkpoint"}, {"Freeway Feather Checkpoint"}},
    ["Freeway to North-West Girders"] = {{"Air Dash, Ground Dash"}},

    ["North-West Girders to Freeway"] = {{"Traffic Blocks"}, {"Air Dash, Ground Dash"}},

    ["North-East Feathers to Freeway"] = {{"Feathers"}, {"Air_Dash"}, {"Ground Dash"}, {"Skid Jump"}},
    ["North-East Feathers to North-East Feathers"] = {{"Feather Maze Checkpoint"}},
    ["North-East Feathers to Badeline Tower Lower"] = {{"Feathers"}, {"Air_Dash"}, {"Ground Dash"}},
    ["North-East Feathers to Badeline Tower Upper"] = {{"Feathers"}},

    ["South-East House to Granny"] = {{"Traffic Blocks"}},
    ["South-East House to South-East House"] = {{"Double Dash House Checkpoint"}},
    ["South-East House to Badeline Tower Lower"] = {{"Air_Dash"}, {"Ground Dash"}},

    ["Badeline Tower Upper to Badeline Tower Upper"] = {{"Badeline Tower Checkpoint"}},
    ["Badeline Tower Upper to Badeline Island"] = {{"Air Dash", "Climb", "Feathers", "Traffic Blocks"}, {"Air Dash", "Climb", "Feathers", "Skid Jump"}, {"Air Dash", "Climb", "Ground Dash", "Traffic Blocks"}, {"Air Dash", "Climb", "Ground Dash", "Skid Jump"}},

    ["Badeline Island to Badeline Tower Upper"] = {{"Air Dash"}, {"Ground Dash"}},
    ["Badeline Island to Badeline Island"] = {{"Badeline Island Checkpoint"}},
}


location_id_to_name = {
    [00] = "First Strawberry",
    [01] = "Floating Blocks Strawberry",
    [02] = "South-East Tower Top Strawberry",
    [03] = "Theo Strawberry",
    [04] = "Fall Through Spike Floor Strawberry",
    [05] = "Troll Strawberry",
    [06] = "Falling Blocks Strawberry",
    [07] = "Traffic Block Strawberry",
    [08] = "South-West Dash Refills Strawberry",
    [09] = "South-East Tower Side Strawberry",
    [10] = "Girders Strawberry",
    [11] = "Badeline Tower Bottom Strawberry",
    [12] = "Breakable Blocks Strawberry",
    [13] = "Feather Maze Strawberry",
    [14] = "Feather Chain Strawberry",
    [15] = "Feather Hidden Strawberry",
    [16] = "Double Dash Puzzle Strawberry",
    [17] = "Double Dash Spike Climb Strawberry",
    [18] = "Double Dash Spring Strawberry",
    [19] = "Badeline Tower Breakable Bottom Strawberry",
    [20] = "Theo Tower Lower Cassette Strawberry",
    [21] = "Theo Tower Upper Cassette Strawberry",
    [22] = "South End of Bridge Cassette Strawberry",
    [23] = "You Are Ready Cassette Strawberry",
    [24] = "Cassette Hidden in the House Strawberry",
    [25] = "North End of Bridge Cassette Strawberry",
    [26] = "Distant Feather Cassette Strawberry",
    [27] = "Feather Arches Cassette Strawberry",
    [28] = "Badeline Tower Cassette Strawberry",
    [29] = "Badeline Cassette Strawberry",

    [100] = "Granny Conversation 1",
    [101] = "Granny Conversation 2",
    [102] = "Granny Conversation 3",
    [103] = "Theo Conversation 1",
    [104] = "Theo Conversation 2",
    [105] = "Theo Conversation 3",
    [106] = "Badeline Conversation 1",
    [107] = "Badeline Conversation 2",
    [108] = "Badeline Conversation 3",

    [200] = "Camera Sign",
    [201] = "Skid Jump Sign",
    [202] = "Dash Jump Sign",
    [203] = "Lonely Sign",
    [204] = "Credits Sign",

    [300] = "Intro Car",
    [301] = "Secret Car",

    [400] = "Intro Checkpoint",
    [401] = "Granny Checkpoint",
    [402] = "South-East Tower Checkpoint",
    [403] = "Climb Sign Checkpoint",
    [404] = "Freeway Checkpoint",
    [405] = "Freeway Feather Checkpoint",
    [406] = "Feather Maze Checkpoint",
    [407] = "Double Dash House Checkpoint",
    [408] = "Badeline Tower Checkpoint",
    [409] = "Badeline Island Checkpoint",

    -- Region Connections
    [1000] = "Intro to Intro",
    [1001] = "Intro to Granny",

    [1011] = "Granny to Granny",
    [1012] = "Granny to Freeway",
    [1013] = "Granny to North-West Girders",
    [1015] = "Granny to South-East House",
    [1016] = "Granny to Badeline Tower Lower",

    [1021] = "Freeway to Granny",
    [1022] = "Freeway to Freeway",
    [1023] = "Freeway to North-West Girders",
    [1024] = "Freeway to North-East Feathers",

    [1032] = "North-West Girders to Freeway",

    [1042] = "North-East Feathers to Freeway",
    [1044] = "North-East Feathers to North-East Feathers",
    [1045] = "North-East Feathers to South-East House",
    [1046] = "North-East Feathers to Badeline Tower Lower",
    [1047] = "North-East Feathers to Badeline Tower Upper",

    [1051] = "South-East House to Granny",
    [1054] = "South-East House to North-East Feathers",
    [1055] = "South-East House to South-East House",
    [1056] = "South-East House to Badeline Tower Lower",

    [1061] = "Badeline Tower Lower to Granny",
    [1064] = "Badeline Tower Lower to North-East Feathers",
    [1065] = "Badeline Tower Lower to South-East House",
    [1067] = "Badeline Tower Lower to Badeline Tower Upper",

    [1071] = "Badeline Tower Upper to Granny",
    [1074] = "Badeline Tower Upper to North-East Feathers",
    [1075] = "Badeline Tower Upper to South-East House",
    [1076] = "Badeline Tower Upper to Badeline Tower Lower",
    [1077] = "Badeline Tower Upper to Badeline Tower Upper",
    [1078] = "Badeline Tower Upper to Badeline Island",

    [1081] = "Badeline Island to Granny",
    [1082] = "Badeline Island to Freeway",
    [1087] = "Badeline Island to Badeline Tower Upper",
    [1088] = "Badeline Island to Badeline Island",
}

item_name_to_code = {
    ["Cannot Access"] = "none",

    ["Dash Refills"]        = "dash_refills",
    ["Double Dash Refills"] = "double_dash_refills",
    ["Feathers"]            = "feathers",
    ["Coins"]               = "coins",
    ["Cassettes"]           = "cassettes",
    ["Traffic Blocks"]      = "traffic_blocks",
    ["Springs"]             = "springs",
    ["Breakable Blocks"]    = "breakable_blocks",

    ["Ground Dash"] = "ground_dash",
    ["Air Dash"]    = "air_dash",
    ["Skid Jump"]   = "skid_jump",
    ["Climb"]       = "climb",

    ["Intro Checkpoint"]             = "checkpoint_1",
    ["Granny Checkpoint"]            = "checkpoint_2",
    ["South-East Tower Checkpoint"]  = "checkpoint_3",
    ["Climb Sign Checkpoint"]        = "checkpoint_4",
    ["Freeway Checkpoint"]           = "checkpoint_5",
    ["Freeway Feather Checkpoint"]   = "checkpoint_6",
    ["Feather Maze Checkpoint"]      = "checkpoint_7",
    ["Double Dash House Checkpoint"] = "checkpoint_8",
    ["Badeline Tower Checkpoint"]    = "checkpoint_9",
    ["Badeline Island Checkpoint"]   = "checkpoint_10",
}


function Logic(location_id)
    local location_name = location_id_to_name[tonumber(location_id)]

    local logic_dict

	local logic_difficulty = Tracker:ProviderCountForCode("logic_difficulty")
	local move_shuffle = Tracker:ProviderCountForCode("move_shuffle")

    if logic_difficulty > 0 then
        logic_dict = location_hard_moves_logic
    else
        logic_dict = location_standard_moves_logic
    end

    local list_of_possible_sets = logic_dict[location_name]

    if list_of_possible_sets == nil then
        return true
    end

    local is_fully_possible = false

    for _, possible_set in ipairs(list_of_possible_sets) do
        local is_possible = true
        for _, item_name in ipairs(possible_set) do
            local item_code = item_name_to_code[item_name]

            local item_count = Tracker:ProviderCountForCode(item_code)

            if item_count == 0 then
                is_possible = false
                break
            end
        end

        if is_possible then
            is_fully_possible = true
            break
        end
    end

    return is_fully_possible
end

function StrawberryCost()
	local strawberries_required = Tracker:ProviderCountForCode("strawberries_required")
	local strawberries = Tracker:ProviderCountForCode("strawberries")
	return (strawberries >= strawberries_required)
end
