The positioning solution doesn't incorporate the GNSS measurements yet.

1. Place the ukf_slam.yaml file in the /params folder of you workspace
2. Use roslaunch to run the ukf_slam.launch file in your workspace.
3. Run slam.py using rosrun.
4. Read the data from the bag. A plot should appear in around 30 seconds. If a higher plotting frequency is desired, reduce "N" in slam.py
