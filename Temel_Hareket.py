from dronekit import connect , VehicleMode , LocationGlobalRelative

drone = connect("127.0.0.1:50000")

drone.mode = VehicleMode("GUIDED")

drone.armed = True

drone.simple_takeoff(20)

kordinat = LocationGlobalRelative(-35.363244, 149.168801, 20)
drone.simple_goto(kordinat, groundspeed=10)

drone.mode = VehicleMode("RTL")
