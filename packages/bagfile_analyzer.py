import rosbag
import os
import statistics


bagFileName = os.environ['BAG_FILE_NAME']
#bagFileName = 'example_rosbag_H3.bag'
dirname = os.path.dirname(__file__)
bagFileDir = os.path.join(dirname, 'bagfiles/' + bagFileName)

#bagfiles
bag = rosbag.Bag(bagFileDir)
bagTopics = bag.get_type_and_topic_info()[1].keys()

print("Found %i topics in bagfile " %len(bagTopics) + bagFileName + "\n")

for topic in bagTopics:

	print(topic + ":")

	timestamps = []
	dt = []
	average_dt = 0.0
	num_messages = 0

	for topic, msg, t in bag.read_messages(topics=[topic]):
		timestamps.append(t)
		num_messages += 1

	for i in range(len(timestamps)-1):
		dt.append( (timestamps[i+1]-timestamps[i]).to_sec() )
		average_dt += dt[i]

	average_dt = round(average_dt/len(dt), 3)
	median_dt = round(statistics.median(dt), 3)
	minimum = round(min(dt),3)
	maximum = round(max(dt),3)

	print("  num_messages: %i" %num_messages)
	print("  period:")
	print("    min: " + str(minimum))
	print("    max: " + str(maximum))
	print("    average: " + str(average_dt))
	print("    median: " + str(median_dt) + "\n")

bag.close()