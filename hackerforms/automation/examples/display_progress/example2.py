from time import sleep

display_progress(0, 10, "Computing values")

# Do some computation
sleep(1)

display_progress(8, 10, "Almost there!")

# Do some other computation
sleep(1)

display("Done")
