
C = int(input(""))
N = int(input(""))
w = {}
total_weight = 0
for i in range(N):
    w[i] = float(input(""))
    total_weight += w[i]
avg_weight = total_weight / N
heaviest = max(w.values())
lightest = min(w.values())
Classification = "Light"
if total_weight >= 200 :
    Classification = "Heavy"

Status = "Shipment can be unloaded"
if total_weight > C:
    Status = "Shipment exceeds port capacity"
print("Total Shipment Weight:" , total_weight)
print("Average Container Weight:" ,avg_weight)
print("Heaviest Container:" , heaviest)
print("Lightest Container:" , lightest)
print("Classification:" , Classification)
print("Port Capacity:" , C)
print("Status:" , Status)
