from dronekit import connect , VehicleMode

drone = connect("127.0.0.1:50000")

drone.mode = VehicleMode("GUIDED")

drone.armed = True

drone.simple_takeoff(5)
