# Write your code here
import json

json_text = input()
stops = json.loads(json_text)

transfer_stops = {}
stop_names = set()
for stop in stops:
    if stop["stop_type"] == "S" or stop["stop_type"] == "F":
        stop_names.add(stop["stop_name"])
    count = transfer_stops.get(stop["stop_name"], 0) + 1
    transfer_stops[stop["stop_name"]] = count

for name, count in transfer_stops.items():
    if count > 1:
        stop_names.add(name)

wrong_stop_names = set()
for stop in stops:
    if stop["stop_type"] == "O" and stop["stop_name"] in stop_names:
        wrong_stop_names.add(stop["stop_name"])


print("On demand stops test:")
if len(wrong_stop_names) != 0:
    print("Wrong stop type:", sorted(wrong_stop_names))
else:
    print("OK")