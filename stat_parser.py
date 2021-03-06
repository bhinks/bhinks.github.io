from datetime import datetime
import json

players = {}
game_map = ""
files = ["console.log.1", "console.log"]
for fname in files:
    f = open(fname, "r")
    for x in f:
        grams = x.split()
        date = grams[0][1:]
        time = date + " " + grams[1][0:-1] + ":00"
        
        if "SpawnServer" in x:
            game_map = grams[-1]
        elif " connected" in x:
            if grams[2] not in players.keys():
                players[grams[2]] = { "kills": [], "deaths": [], "suicides": [], "sessions": [], "opponents": {}, "weapons": {}, "maps": {} }
            players[grams[2]]["sessions"].append({ "start": time})
        elif " disconnected" in x:
            if grams[2] in players.keys():
                start = datetime.strptime(players[grams[2]]["sessions"][-1]["start"], "%Y-%m-%d %H:%M:%S")
                end = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
                diff = end - start
                minutes = diff.total_seconds() / 60
                players[grams[2]]["sessions"][-1]["duration"] = minutes
        elif " ate " in x:
            player2 = grams[4][0:-2]
            players[grams[2]]["deaths"].append({ "player": player2, 
                                                "weapon": "Rocket Launcher", 
                                                "date": date, 
                                                "map": game_map})
            players[player2]["kills"].append({ "player": grams[2], 
                                                "weapon": "Rocket Launcher", 
                                                "date": date, 
                                                "map": game_map})
        elif " almost dodged " in x:
            player2 = grams[5][0:-2]
            players[grams[2]]["deaths"].append({ "player": player2, 
                                                "weapon": "Rocket Launcher", 
                                                "date": date, 
                                                "map": game_map})
            players[player2]["kills"].append({ "player": grams[2], 
                                                "weapon": "Rocket Launcher", 
                                                "date": date, 
                                                "map": game_map})
        elif " blew h" in x:
            players[grams[2]]["suicides"].append({ "player": grams[2], 
                                                "weapon": "Rocket Launcher", 
                                                "date": date, 
                                                "map": game_map})
        elif " was railed " in x:
            player2 = grams[6]
            players[grams[2]]["deaths"].append({ "player": player2, 
                                                "weapon": "Railgun", 
                                                "date": date, 
                                                "map": game_map})
            players[player2]["kills"].append({ "player": grams[2], 
                                                "weapon": "Railgun", 
                                                "date": date, 
                                                "map": game_map})
        elif " was melted by " in x:
            player2 = grams[6][0:-2]
            players[grams[2]]["deaths"].append({ "player": player2, 
                                                "weapon": "Hyperblaster", 
                                                "date": date, 
                                                "map": game_map})
            players[player2]["kills"].append({ "player": grams[2], 
                                                "weapon": "Hyperblaster", 
                                                "date": date, 
                                                "map": game_map})
        elif " was blasted " in x:
            player2 = grams[6]
            players[grams[2]]["deaths"].append({ "player": player2, 
                                                "weapon": "Blaster", 
                                                "date": date, 
                                                "map": game_map})
            players[player2]["kills"].append({ "player": grams[2], 
                                                "weapon": "Blaster", 
                                                "date": date, 
                                                "map": game_map})
        elif " was gunned down " in x:
            player2 = grams[7]
            players[grams[2]]["deaths"].append({ "player": player2, 
                                                "weapon": "Shotgun", 
                                                "date": date, 
                                                "map": game_map})
            players[player2]["kills"].append({ "player": grams[2], 
                                                "weapon": "Shotgun", 
                                                "date": date, 
                                                "map": game_map})
        elif " was blown away " in x:
            player2 = grams[7][0:-2]
            players[grams[2]]["deaths"].append({ "player": player2, 
                                                "weapon": "Super Shotgun", 
                                                "date": date, 
                                                "map": game_map})
            players[player2]["kills"].append({ "player": grams[2], 
                                                "weapon": "Super Shotgun", 
                                                "date": date, 
                                                "map": game_map})
        elif " was machinegunned " in x:
            player2 = grams[6]
            players[grams[2]]["deaths"].append({ "player": player2, 
                                                "weapon": "Machinegun", 
                                                "date": date, 
                                                "map": game_map})
            players[player2]["kills"].append({ "player": grams[2], 
                                                "weapon": "Machinegun", 
                                                "date": date, 
                                                "map": game_map})
        elif " was cut in half " in x:
            player2 = grams[8][0:-2]
            players[grams[2]]["deaths"].append({ "player": player2, 
                                                "weapon": "Chaingun", 
                                                "date": date, 
                                                "map": game_map})
            players[player2]["kills"].append({ "player": grams[2], 
                                                "weapon": "Chaingun", 
                                                "date": date, 
                                                "map": game_map})
        elif " was popped " in x:
            player2 = grams[6][0:-2]
            players[grams[2]]["deaths"].append({ "player": player2, 
                                                "weapon": "Grenade Launcher", 
                                                "date": date, 
                                                "map": game_map})
            players[player2]["kills"].append({ "player": grams[2], 
                                                "weapon": "Grenade Launcher", 
                                                "date": date, 
                                                "map": game_map})
        elif " was shredded " in x:
            player2 = grams[6][0:-2]
            players[grams[2]]["deaths"].append({ "player": player2, 
                                                "weapon": "Grenade Launcher", 
                                                "date": date, 
                                                "map": game_map})
            players[player2]["kills"].append({ "player": grams[2], 
                                                "weapon": "Grenade Launcher", 
                                                "date": date, 
                                                "map": game_map})
        elif " saw the pretty lights " in x:
            player2 = grams[8][0:-2]
            players[grams[2]]["deaths"].append({ "player": player2, 
                                                "weapon": "BFG", 
                                                "date": date, 
                                                "map": game_map})
            players[player2]["kills"].append({ "player": grams[2], 
                                                "weapon": "BFG", 
                                                "date": date, 
                                                "map": game_map})
        elif " was disintegrated " in x:
            player2 = grams[6][0:-2]
            players[grams[2]]["deaths"].append({ "player": player2, 
                                                "weapon": "BFG", 
                                                "date": date, 
                                                "map": game_map})
            players[player2]["kills"].append({ "player": grams[2], 
                                                "weapon": "BFG", 
                                                "date": date, 
                                                "map": game_map})
        elif " couldn't hide from " in x:
            player2 = grams[6][0:-2]
            players[grams[2]]["deaths"].append({ "player": player2, 
                                                "weapon": "BFG", 
                                                "date": date, 
                                                "map": game_map})
            players[player2]["kills"].append({ "player": grams[2], 
                                                "weapon": "BFG", 
                                                "date": date, 
                                                "map": game_map})
        elif " didn't see " in x:
            player2 = grams[5][0:-2]
            players[grams[2]]["deaths"].append({ "player": player2, 
                                                "weapon": "Handgrenade", 
                                                "date": date, 
                                                "map": game_map})
            players[player2]["kills"].append({ "player": grams[2], 
                                                "weapon": "Handgrenade", 
                                                "date": date, 
                                                "map": game_map})
        elif " caught " in x:
            player2 = grams[4][0:-2]
            players[grams[2]]["deaths"].append({ "player": player2, 
                                                "weapon": "Handgrenade", 
                                                "date": date, 
                                                "map": game_map})
            players[player2]["kills"].append({ "player": grams[2], 
                                                "weapon": "Handgrenade", 
                                                "date": date, 
                                                "map": game_map})
        elif " tried to invade " in x:
            player2 = grams[6][0:-2]
            players[grams[2]]["deaths"].append({ "player": player2, 
                                                "weapon": "Telefrag", 
                                                "date": date, 
                                                "map": game_map})
            players[player2]["kills"].append({ "player": grams[2], 
                                                "weapon": "Telefrag", 
                                                "date": date, 
                                                "map": game_map})
        elif " tried to put the pin " in x:
            players[grams[2]]["suicides"].append({ "player": grams[2], 
                                                "weapon": "Handgrenade", 
                                                "date": date, 
                                                "map": game_map})
        elif " tripped on h" in x:
            players[grams[2]]["suicides"].append({ "player": grams[2], 
                                                "weapon": "Grenade Launcher", 
                                                "date": date, 
                                                "map": game_map})
        elif " should have used a smaller " in x:
            players[grams[2]]["suicides"].append({ "player": grams[2], 
                                                "weapon": "BFG", 
                                                "date": date, 
                                                "map": game_map})
        elif " melted" in x:
            players[grams[2]]["suicides"].append({ "player": grams[2], 
                                                "weapon": "Acid", 
                                                "date": date, 
                                                "map": game_map})
        elif " cratered" in x:
            players[grams[2]]["suicides"].append({ "player": grams[2], 
                                                "weapon": "Fall", 
                                                "date": date, 
                                                "map": game_map})
        elif " was squished" in x:
            players[grams[2]]["suicides"].append({ "player": grams[2], 
                                                "weapon": "Crush", 
                                                "date": date, 
                                                "map": game_map})
        elif " sank like a rock" in x:
            players[grams[2]]["suicides"].append({ "player": grams[2], 
                                                "weapon": "Water", 
                                                "date": date, 
                                                "map": game_map})
        elif " does a back flip" in x:
            players[grams[2]]["suicides"].append({ "player": grams[2], 
                                                "weapon": "Lava", 
                                                "date": date, 
                                                "map": game_map})
records = {
    "weapons": {
        "Blaster": {"kills_player": "", "kills_count": 0, "deaths_player": "", "deaths_count": 0},
        "Shotgun":  {"kills_player": "", "kills_count": 0, "deaths_player": "", "deaths_count": 0},
        "Super Shotgun":  {"kills_player": "", "kills_count": 0, "deaths_player": "", "deaths_count": 0},
        "Machinegun":  {"kills_player": "", "kills_count": 0, "deaths_player": "", "deaths_count": 0},
        "Chaingun":  {"kills_player": "", "kills_count": 0, "deaths_player": "", "deaths_count": 0},
        "Handgrenade":  {"kills_player": "", "kills_count": 0, "deaths_player": "", "deaths_count": 0},
        "Grenade Launcher":  {"kills_player": "", "kills_count": 0, "deaths_player": "", "deaths_count": 0},
        "Rocket Launcher":  {"kills_player": "", "kills_count": 0, "deaths_player": "", "deaths_count": 0},
        "Hyperblaster":  {"kills_player": "", "kills_count": 0, "deaths_player": "", "deaths_count": 0},
        "Railgun":  {"kills_player": "", "kills_count": 0, "deaths_player": "", "deaths_count": 0},
        "BFG":  {"kills_player": "", "kills_count": 0, "deaths_player": "", "deaths_count": 0},
        "Acid":  {"kills_player": "", "kills_count": 0, "deaths_player": "", "deaths_count": 0},
        "Lava":  {"kills_player": "", "kills_count": 0, "deaths_player": "", "deaths_count": 0},
        "Crush":  {"kills_player": "", "kills_count": 0, "deaths_player": "", "deaths_count": 0},
        "Fall":  {"kills_player": "", "kills_count": 0, "deaths_player": "", "deaths_count": 0},
        "Water":  {"kills_player": "", "kills_count": 0, "deaths_player": "", "deaths_count": 0},
    },
    "maps": {
        "q2dm1": {"kills_player": "", "kills_count": 0, "deaths_player": "", "deaths_count": 0},
        "q2dm2":  {"kills_player": "", "kills_count": 0, "deaths_player": "", "deaths_count": 0},
        "rocketcourt":  {"kills_player": "", "kills_count": 0, "deaths_player": "", "deaths_count": 0},
        "aeroq2":  {"kills_player": "", "kills_count": 0, "deaths_player": "", "deaths_count": 0},
        "ztn2dm1":  {"kills_player": "", "kills_count": 0, "deaths_player": "", "deaths_count": 0},
        "q2dm7":  {"kills_player": "", "kills_count": 0, "deaths_player": "", "deaths_count": 0},
        "ztn2dm5":  {"kills_player": "", "kills_count": 0, "deaths_player": "", "deaths_count": 0},
        "q2dm8":  {"kills_player": "", "kills_count": 0, "deaths_player": "", "deaths_count": 0},
        "match1":  {"kills_player": "", "kills_count": 0, "deaths_player": "", "deaths_count": 0},
        "q2dm3":  {"kills_player": "", "kills_count": 0, "deaths_player": "", "deaths_count": 0},
        "ztn2dm2":  {"kills_player": "", "kills_count": 0, "deaths_player": "", "deaths_count": 0},
        "ztn2dm3":  {"kills_player": "", "kills_count": 0, "deaths_player": "", "deaths_count": 0},
        "q2dm1mirrored":  {"kills_player": "", "kills_count": 0, "deaths_player": "", "deaths_count": 0},
        "ztn2dm4":  {"kills_player": "", "kills_count": 0, "deaths_player": "", "deaths_count": 0}
    },
    "overall": {
        "most_kills": { "player": "", "count": 0},
        "most_deaths": { "player": "", "count": 0},
        "most_suicides": { "player": "", "count": 0},
        "highest_kdr": { "player": "", "count": 0},
        "highest_kph": { "player": "", "count": 0}
    }
}

for player in players.keys():
    if "duration" not in players[player]["sessions"][-1].keys():
        start = datetime.strptime(players[player]["sessions"][-1]["start"], "%Y-%m-%d %H:%M:%S")
        end = datetime.now()
        diff = end - start
        minutes = diff.total_seconds() / 60
        players[player]["sessions"][-1]["duration"] = minutes

    players[player]["total_kills"] = len(players[player]["kills"])
    players[player]["total_deaths"] = len(players[player]["deaths"]) + len(players[player]["suicides"])
    players[player]["total_suicides"] = len(players[player]["suicides"])
    
    minutes = 0
    for session in players[player]["sessions"]:
        minutes += session["duration"]
    players[player]["total_minutes"] = minutes

    if players[player]["total_deaths"] == 0:
        players[player]["total_kdr"] = format(players[player]["total_kills"], '.2f')
    else:
        players[player]["total_kdr"] = format((players[player]["total_kills"] / players[player]["total_deaths"]), '.2f')    
    players[player]["total_kph"] = format((players[player]["total_kills"] / (players[player]["total_minutes"] / 60 )), '.2f')
    players[player]["total_dph"] = format((players[player]["total_deaths"] / (players[player]["total_minutes"] / 60 )), '.2f')

    if players[player]["total_kills"] >= records["overall"]["most_kills"]["count"]:
        records["overall"]["most_kills"]["count"] = players[player]["total_kills"]
        records["overall"]["most_kills"]["player"] = player
    if players[player]["total_deaths"] >= records["overall"]["most_deaths"]["count"]:
        records["overall"]["most_deaths"]["count"] = players[player]["total_deaths"]
        records["overall"]["most_deaths"]["player"] = player
    if players[player]["total_suicides"] >= records["overall"]["most_suicides"]["count"]:
        records["overall"]["most_suicides"]["count"] = players[player]["total_suicides"]
        records["overall"]["most_suicides"]["player"] = player
    if float(players[player]["total_kdr"]) >= float(records["overall"]["highest_kdr"]["count"]):
        records["overall"]["highest_kdr"]["count"] = players[player]["total_kdr"]
        records["overall"]["highest_kdr"]["player"] = player
    if float(players[player]["total_kph"]) >= float(records["overall"]["highest_kph"]["count"]):
        records["overall"]["highest_kph"]["count"] = players[player]["total_kph"]
        records["overall"]["highest_kph"]["player"] = player

    for killed in players[player]["kills"]:
        if killed["player"] not in players[player]["opponents"].keys():
            players[player]["opponents"][killed["player"]] = { "kills": 0, "deaths": 0}
        if killed["weapon"] not in players[player]["weapons"].keys():
            players[player]["weapons"][killed["weapon"]] = { "kills": 0, "deaths": 0}
        if killed["map"] not in players[player]["maps"].keys():
            players[player]["maps"][killed["map"]] = { "kills": 0, "deaths": 0}
        players[player]["opponents"][killed["player"]]["kills"] += 1
        players[player]["weapons"][killed["weapon"]]["kills"] += 1
        players[player]["maps"][killed["map"]]["kills"] += 1
        if players[player]["weapons"][killed["weapon"]]["kills"] > records["weapons"][killed["weapon"]]["kills_count"]:
            records["weapons"][killed["weapon"]]["kills_player"] = player
            records["weapons"][killed["weapon"]]["kills_count"] = players[player]["weapons"][killed["weapon"]]["kills"]
        if players[player]["maps"][killed["map"]]["kills"] > records["maps"][killed["map"]]["kills_count"]:
            records["maps"][killed["map"]]["kills_player"] = player
            records["maps"][killed["map"]]["kills_count"] = players[player]["maps"][killed["map"]]["kills"]
    
    for died in players[player]["deaths"]:
        if died["player"] not in players[player]["opponents"].keys():
            players[player]["opponents"][died["player"]] = { "kills": 0, "deaths": 0}
        if died["weapon"] not in players[player]["weapons"].keys():
            players[player]["weapons"][died["weapon"]] = { "kills": 0, "deaths": 0}
        if died["map"] not in players[player]["maps"].keys():
            players[player]["maps"][died["map"]] = { "kills": 0, "deaths": 0}
        players[player]["opponents"][died["player"]]["deaths"] += 1
        players[player]["weapons"][died["weapon"]]["deaths"] += 1
        players[player]["maps"][died["map"]]["deaths"] += 1
        if players[player]["weapons"][died["weapon"]]["deaths"] > records["weapons"][died["weapon"]]["deaths_count"]:
            records["weapons"][died["weapon"]]["deaths_player"] = player
            records["weapons"][died["weapon"]]["deaths_count"] = players[player]["weapons"][died["weapon"]]["deaths"]
        if players[player]["maps"][died["map"]]["deaths"] > records["maps"][died["map"]]["deaths_count"]:
            records["maps"][died["map"]]["deaths_player"] = player
            records["maps"][died["map"]]["deaths_count"] = players[player]["maps"][died["map"]]["deaths"]
    
    for died in players[player]["suicides"]:
        if died["weapon"] not in players[player]["weapons"].keys():
            players[player]["weapons"][died["weapon"]] = { "kills": 0, "deaths": 0}
        if died["map"] not in players[player]["maps"].keys():
            players[player]["maps"][died["map"]] = { "kills": 0, "deaths": 0}
        players[player]["weapons"][died["weapon"]]["deaths"] += 1
        players[player]["maps"][died["map"]]["deaths"] += 1
        if players[player]["weapons"][died["weapon"]]["deaths"] > records["weapons"][died["weapon"]]["deaths_count"]:
            records["weapons"][died["weapon"]]["deaths_player"] = player
            records["weapons"][died["weapon"]]["deaths_count"] = players[player]["weapons"][died["weapon"]]["deaths"]
        if players[player]["maps"][died["map"]]["deaths"] > records["maps"][died["map"]]["deaths_count"]:
            records["maps"][died["map"]]["deaths_player"] = player
            records["maps"][died["map"]]["deaths_count"] = players[player]["maps"][died["map"]]["deaths"]


with open("assets/stats.json", "w") as f:
    json.dump({ "players": players, "records": records }, f)
    