pluto_earth = 4800000000
c = 300000  # km/s

total_seconds = pluto_earth / c

hours = int(total_seconds // 3600)
minutes = int((total_seconds % 3600) // 60)

print("지구에서 명왕성까지 걸리는 시간", hours, "시간", minutes, "분")