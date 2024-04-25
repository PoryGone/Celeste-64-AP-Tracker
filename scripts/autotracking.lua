ScriptHost:LoadScript("scripts/autotracking/item_mapping.lua")
ScriptHost:LoadScript("scripts/autotracking/location_mapping.lua")

LEVEL_UNLOCKS = {}



CUR_INDEX = -1
SLOT_DATA = nil


function onClear(slot_data)
    SLOT_DATA = slot_data
    CUR_INDEX = -1

    for _, v in pairs(ITEM_MAPPING) do
        if v[1] then
            local obj = Tracker:FindObjectForCode(v[1])
            if obj then
                if v[2] == "toggle" then
                    obj.Active = false
                elseif v[2] == "progressive" then
                    if obj.Active then
                        obj.CurrentStage = 0
                    --else
                    --    obj.Active = true
                    end
                elseif v[2] == "consumable" then
                    obj.AcquiredCount = 0
                end
            end
        end
    end
    for _, v in pairs(SETTINGS_MAPPING) do
        if v[1] then
            local obj = Tracker:FindObjectForCode(v[1])
            if obj then
                obj.AcquiredCount = 0
            end
        end
    end

    for k, v in pairs(LOCATION_MAPPING) do
        local loc_list = LOCATION_MAPPING[k]
        for i, loc in ipairs(loc_list) do
            if loc:sub(1, 1) == "@" then
                local obj = Tracker:FindObjectForCode(loc)
                if obj then
                    obj.AvailableChestCount = obj.ChestCount
                end
            end
        end
    end

    if SLOT_DATA == nil then
        return
    end

    if slot_data['strawberries_required'] then
        local strawberries_required = Tracker:FindObjectForCode("strawberries_required")
        if strawberries_required then
            strawberries_required.AcquiredCount = (slot_data['strawberries_required'])
        end
    end

    if slot_data['logic_difficulty'] then
        local logic_difficulty = Tracker:FindObjectForCode("logic_difficulty")
        logic_difficulty.Active = (slot_data['logic_difficulty'] ~= 0)
    end

    if slot_data['move_shuffle'] then
        local move_shuffle = Tracker:FindObjectForCode("move_shuffle")
        move_shuffle.Active = (slot_data['move_shuffle'] ~= 0)
    end

    if slot_data['friendsanity'] then
        local friendsanity = Tracker:FindObjectForCode("friendsanity")
        friendsanity.Active = (slot_data['friendsanity'] ~= 0)
    end

    if slot_data['signsanity'] then
        local signsanity = Tracker:FindObjectForCode("signsanity")
        signsanity.Active = (slot_data['signsanity'] ~= 0)
    end

    if slot_data['carsanity'] then
        local carsanity = Tracker:FindObjectForCode("carsanity")
        carsanity.Active = (slot_data['carsanity'] ~= 0)
    end

end

function onItem(index, item_id, item_name, player_number)
    if index <= CUR_INDEX then return end
    local is_local = player_number == Archipelago.PlayerNumber
    CUR_INDEX = index;
    
    local v = ITEM_MAPPING[item_id]
    if not v then
        return
    end

    if not v[1] then
        return
    end

    local obj = Tracker:FindObjectForCode(v[1])
    if obj then
        if v[2] == "toggle" then
            obj.Active = true
        elseif v[2] == "progressive" then
            if obj.Active then
                obj.CurrentStage = obj.CurrentStage + 1
            else
                obj.Active = true
            end
        elseif v[2] == "consumable" then
            obj.AcquiredCount = obj.AcquiredCount + obj.Increment
        end
    end
end

function onLocation(location_id, location_name)
    local location_array = LOCATION_MAPPING[location_id]
    if not location_array or not location_array[1] then
        print(string.format("onLocation: could not find location mapping for id %s", location_id))
        return
    end

    for _, location in pairs(location_array) do
        local obj = Tracker:FindObjectForCode(location)
        if obj then
            if location:sub(1,1) == "@" then
                obj.AvailableChestCount = obj.AvailableChestCount - 1 
            else
                obj.Active = true
            end
        else 
            print(string.format("onLocation: could not find object for code %s", location))
        end
    end
end


Archipelago:AddClearHandler("clear handler", onClear)
Archipelago:AddItemHandler("item handler", onItem)
Archipelago:AddLocationHandler("location handler", onLocation)
