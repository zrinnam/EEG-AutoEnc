
# # timestamps with long response periods removed and non trial period responses left in
# timestamps = [0, 13146, 15569, 18194, 18720, 21455, 21991, 24784, 25438, 
#               27956, 28746, 31145, 31957, 33639, 34049, 37277, 38067, 
#               40288, 40878, 44117, 44452, 46688, 46997, 49050, 49375, 
#               51076, 51738, 53301, 53645, 56163, 56416, 59405, 60214, 
#               63455, 64201, 66834, 69328, 72717, 74145, 78014, 79477, 
#               80405, 82955, 83823, 84869, 86783, 87931, 88390, 91525, 
#               91760, 95086, 96227, 99359, 99651, 102772, 103909, 106184, 
#               106814, 109239, 109425, 110005, 111685, 111912, 114611, 
#               115660, 118441, 118475, 122981, 123363, 125035, 126463, 
#               128967, 132195, 134699, 137859, 144537, 144995, 148171, 
#               149215, 151616, 152369, 153808, 156285, 157227, 160349, 
#               161088, 162746, 163152, 165174, 165847, 167852, 168201, 
#               169994, 170314, 173607, 174223, 176532, 177360, 180735, 
#               181081, 182988, 183295, 185354, 186150, 188076, 188744, 
#               191113, 193617, 196869, 202124, 202499, 205760, 206090, 
#               207668, 207956, 211343, 211600, 214218, 214769, 217331, 
#               217856, 219557, 220346, 223642, 223985, 226545, 227347, 
#               229466, 230205, 233711, 234056, 237012, 237073, 240139, 
#               242640, 245890, 247268, 251742, 252123, 253180, 254136, 
#               254852, 257780, 258814, 260424, 260465, 261479, 263313, 
#               263747, 266339, 266636, 269752, 270660, 271456, 273907, 
#               274146, 276216, 276672, 279055, 279570, 281751, 282362, 
#               284651, 285396, 289103, 291602, 294651, 300750, 301606, 
#               303385, 303717, 305890, 306664, 308957, 309459, 311250, 
#               311434, 313988, 314298,316042, 316509, 319696, 320199, 
#               323227, 323779, 326030, 326341, 328762, 329757, 331563, 
#               331809, 335040, 335346,337760, 340263, 343389, 345889, 
#               349484, 353288, 355806, 356054, 358673, 359401, 362703, 
#               362773, 364181, 365792, 366538, 368546, 368945, 371806, 
#               372178, 374560, 375306, 375615, 378165, 378690, 382086, 
#               82352, 383906,384259, 386516, 387458, 390838, 391652, 
#               394648, 395492, 398692, 398992, 400437, 401453, 401976, 
#               407008, 409511,413070, 415768, 417847, 418225, 421406, 
#               422202, 424928, 425182, 427541, 428115, 429084, 430842, 
#               431743, 433495, 433806, 436684, 436983, 439429, 439878, 
#               442036, 442851, 445459, 445751, 447736, 448568, 450474, 
#               450785,453479, 454390, 455404, 457217, 457515, 459527, 
#               459804, 461458, 463958]


data = """
Timestamp: 0, Event ID: 10020, Description: Segment start
Timestamp: 0, Event ID: 99999, Description: Segment starts (initial event)
Timestamp differences start here
Timestamp: 13146, Event ID: 10001, Description: Start of song playback
*Timestamp: 15569, Event ID: 10006, Description: Response during non-trial period (arrow up)
Timestamp: 18194, Event ID: 10012, Description: Start of trial period (short increase)
Timestamp: 18720, Event ID: 10014, Description: Response
Timestamp: 21455, Event ID: 10007, Description: Start of trial period (long decrease)
Timestamp: 21991, Event ID: 10008, Description: Response
Timestamp: 24784, Event ID: 10016, Description: Start of trial period (long increase)
Timestamp: 25438, Event ID: 10018, Description: Response
Timestamp: 27956, Event ID: 10016, Description: Start of trial period (long increase)
Timestamp: 28746, Event ID: 10018, Description: Response
Timestamp: 31145, Event ID: 10012, Description: Start of trial period (short increase)
Timestamp: 31957, Event ID: 10014, Description: Response
Timestamp: 33639, Event ID: 10012, Description: Start of trial period (short increase)
Timestamp: 34049, Event ID: 10014, Description: Response
Timestamp: 37277, Event ID: 10016, Description: Start of trial period (long increase)
Timestamp: 38067, Event ID: 10018, Description: Response
Timestamp: 40288, Event ID: 10016, Description: Start of trial period (long increase)
Timestamp: 40878, Event ID: 10018, Description: Response
Timestamp: 44117, Event ID: 10012, Description: Start of trial period (short increase)
Timestamp: 44452, Event ID: 10014, Description: Response
Timestamp: 46688, Event ID: 10012, Description: Start of trial period (short increase)
Timestamp: 46997, Event ID: 10014, Description: Response
Timestamp: 49050, Event ID: 10012, Description: Start of trial period (short increase)
Timestamp: 49375, Event ID: 10014, Description: Response
Timestamp: 51076, Event ID: 10016, Description: Start of trial period (long increase)
Timestamp: 51738, Event ID: 10018, Description: Response
Timestamp: 53301, Event ID: 10016, Description: Start of trial period (long increase)
Timestamp: 53645, Event ID: 10018, Description: Response
Timestamp: 56163, Event ID: 10012, Description: Start of trial period (short increase)
Timestamp: 56416, Event ID: 10014, Description: Response
Timestamp: 59405, Event ID: 10007, Description: Start of trial period (long decrease)
Timestamp: 60214, Event ID: 10008, Description: Response
Timestamp: 63455, Event ID: 10016, Description: Start of trial period (long increase)
Timestamp: 64201, Event ID: 10018, Description: Response
Timestamp: 66834, Event ID: 10012, Description: Start of trial period (short increase)
Timestamp: 69328, Event ID: 10015, Description: End of trial period (no response, aka a miss)
Timestamp: 72717, Event ID: 10001, Description: Start of song playback
*Timestamp: 74145, Event ID: 10006, Description: Response during non-trial period (arrow up)
*Timestamp: 78014, Event ID: 10006, Description: Response during non-trial period (arrow up)
Timestamp: 79477, Event ID: 10007, Description: Start of trial period (long decrease)
Timestamp: 80405, Event ID: 10008, Description: Response
*Timestamp: 82955, Event ID: 10011, Description: Response during non-trial period (arrow down)
Timestamp: 83823, Event ID: 10007, Description: Start of trial period (long decrease)
Timestamp: 84869, Event ID: 10008, Description: Response
*Timestamp: 86783, Event ID: 10011, Description: Response during non-trial period (arrow down)
Timestamp: 87931, Event ID: 10002, Description: Start of trial period (short decrease)
Timestamp: 88390, Event ID: 10003, Description: Response
Timestamp: 91525, Event ID: 10012, Description: Start of trial period (short increase)
Timestamp: 91760, Event ID: 10014, Description: Response
Timestamp: 95086, Event ID: 10007, Description: Start of trial period (long decrease)
Timestamp: 96227, Event ID: 10008, Description: Response
Timestamp: 99359, Event ID: 10002, Description: Start of trial period (short decrease)
Timestamp: 99651, Event ID: 10004, Description: Response
Weird period of response button presses, skipping to next volume event
Timestamp: 102772, Event ID: 10007, Description: Start of trial period (long decrease)
Timestamp: 103909, Event ID: 10008, Description: Response
Timestamp: 106184, Event ID: 10012, Description: Start of trial period (short increase)
Timestamp: 106814, Event ID: 10014, Description: Response
*Timestamp: 109239, Event ID: 10011, Description: Response during non-trial period (arrow down)
Timestamp: 109425, Event ID: 10002, Description: Start of trial period (short decrease)
Timestamp: 110005, Event ID: 10003, Description: Response
Timestamp: 111685, Event ID: 10012, Description: Start of trial period (short increase)
Timestamp: 111912, Event ID: 10014, Description: Response
Timestamp: 114611, Event ID: 10016, Description: Start of trial period (long increase)
Timestamp: 115660, Event ID: 10018, Description: Response
Timestamp: 118441, Event ID: 10007, Description: Start of trial period (long decrease)
Timestamp: 118475, Event ID: 10009, Description: Response
Weird period of response button presses, skipping to next volume event
Timestamp: 122981, Event ID: 10002, Description: Start of trial period (short decrease)
Timestamp: 123363, Event ID: 10003, Description: Response
*Timestamp: 125035, Event ID: 10006, Description: Response during non-trial period (arrow up)
Timestamp: 126463, Event ID: 10002, Description: Start of trial period (short decrease)
Timestamp: 128967, Event ID: 10005, Description: End of trial period (no response, aka a miss)
Timestamp: 132195, Event ID: 10007, Description: Start of trial period (long decrease)
Timestamp: 134699, Event ID: 10010, Description: End of trial period (no response, aka a miss)
Timestamp: 137859, Event ID: 10001, Description: Start of song playback
Weird period of response button presses, skipping to next volume event
Timestamp: 144537, Event ID: 10012, Description: Start of trial period (short increase)
Timestamp: 144995, Event ID: 10014, Description: Response
Timestamp: 148171, Event ID: 10016, Description: Start of trial period (long increase)
Timestamp: 149215, Event ID: 10018, Description: Response
*Timestamp: 151616, Event ID: 10011, Description: Response during non-trial period (arrow down)
Timestamp: 152369, Event ID: 10016, Description: Start of trial period (long increase)
Timestamp: 153808, Event ID: 10018, Description: Response
Timestamp: 156285, Event ID: 10016, Description: Start of trial period (long increase)
Timestamp: 157227, Event ID: 10018, Description: Response
Timestamp: 160349, Event ID: 10012, Description: Start of trial period (short increase)
Timestamp: 161088, Event ID: 10014, Description: Response
Timestamp: 162746, Event ID: 10002, Description: Start of trial period (short decrease)
Timestamp: 163152, Event ID: 10003, Description: Response
Timestamp: 165174, Event ID: 10016, Description: Start of trial period (long increase)
Timestamp: 165847, Event ID: 10018, Description: Response
Timestamp: 167852, Event ID: 10002, Description: Start of trial period (short decrease)
Timestamp: 168201, Event ID: 10003, Description: Response
Timestamp: 169994, Event ID: 10002, Description: Start of trial period (short decrease)
Timestamp: 170314, Event ID: 10003, Description: Response
Timestamp: 173607, Event ID: 10016, Description: Start of trial period (long increase)
Timestamp: 174223, Event ID: 10018, Description: Response
Timestamp: 176532, Event ID: 10016, Description: Start of trial period (long increase)
Timestamp: 177360, Event ID: 10018, Description: Response
Timestamp: 180735, Event ID: 10012, Description: Start of trial period (short increase)
Timestamp: 181081, Event ID: 10014, Description: Response
Timestamp: 182988, Event ID: 10007, Description: Start of trial period (long decrease)
Timestamp: 183295, Event ID: 10008, Description: Response
Timestamp: 185354, Event ID: 10016, Description: Start of trial period (long increase)
Timestamp: 186150, Event ID: 10018, Description: Response
Timestamp: 188076, Event ID: 10016, Description: Start of trial period (long increase)
Timestamp: 188744, Event ID: 10018, Description: Response
Timestamp: 191113, Event ID: 10012, Description: Start of trial period (short increase)
Timestamp: 193617, Event ID: 10015, Description: End of trial period (no response, aka a miss)
Timestamp: 196869, Event ID: 10001, Description: Start of song playback
Timestamp: 202124, Event ID: 10002, Description: Start of trial period (short decrease)
Timestamp: 202499, Event ID: 10003, Description: Response
Timestamp: 205760, Event ID: 10002, Description: Start of trial period (short decrease)
Timestamp: 206090, Event ID: 10003, Description: Response
Timestamp: 207668, Event ID: 10012, Description: Start of trial period (short increase)
Timestamp: 207956, Event ID: 10014, Description: Response
Timestamp: 211343, Event ID: 10002, Description: Start of trial period (short decrease)
Timestamp: 211600, Event ID: 10003, Description: Response
Timestamp: 214218, Event ID: 10007, Description: Start of trial period (long decrease)
Timestamp: 214769, Event ID: 10008, Description: Response
Timestamp: 217331, Event ID: 10007, Description: Start of trial period (long decrease)
Timestamp: 217856, Event ID: 10008, Description: Response
Timestamp: 219557, Event ID: 10007, Description: Start of trial period (long decrease)
Timestamp: 220346, Event ID: 10008, Description: Response
Timestamp: 223642, Event ID: 10002, Description: Start of trial period (short decrease)
Timestamp: 223985, Event ID: 10003, Description: Response
Timestamp: 226545, Event ID: 10002, Description: Start of trial period (short decrease)
Timestamp: 227347, Event ID: 10003, Description: Response
Timestamp: 229466, Event ID: 10007, Description: Start of trial period (long decrease)
Timestamp: 230205, Event ID: 10008, Description: Response
Timestamp: 233711, Event ID: 10002, Description: Start of trial period (short decrease)
Timestamp: 234056, Event ID: 10003, Description: Response
Timestamp: 237012, Event ID: 10007, Description: Start of trial period (long decrease)
Timestamp: 237073, Event ID: 10008, Description: Response
Timestamp: 240139, Event ID: 10002, Description: Start of trial period (short decrease)
Timestamp: 242640, Event ID: 10005, Description: End of trial period (no response, aka a miss)
Timestamp: 245890, Event ID: 10001, Description: Start of song playback
*Timestamp: 247268, Event ID: 10006, Description: Response during non-trial period (arrow up)
Timestamp: 251742, Event ID: 10012, Description: Start of trial period (short increase)
Timestamp: 252123, Event ID: 10014, Description: Response
*Timestamp: 253180, Event ID: 10006, Description: Response during non-trial period (arrow up)
Timestamp: 254136, Event ID: 10016, Description: Start of trial period (long increase)
Timestamp: 254852, Event ID: 10018, Description: Response
Timestamp: 257780, Event ID: 10016, Description: Start of trial period (long increase)
Timestamp: 258814, Event ID: 10018, Description: Response
*Timestamp: 260424, Event ID: 10006, Description: Response during non-trial period (arrow up)
Timestamp: 260465, Event ID: 10016, Description: Start of trial period (long increase)
Timestamp: 261479, Event ID: 10018, Description: Response
Timestamp: 263313, Event ID: 10012, Description: Start of trial period (short increase)
Timestamp: 263747, Event ID: 10014, Description: Response
Timestamp: 266339, Event ID: 10012, Description: Start of trial period (short increase)
Timestamp: 266636, Event ID: 10014, Description: Response
Timestamp: 269752, Event ID: 10016, Description: Start of trial period (long increase)
Timestamp: 270660, Event ID: 10018, Description: Response
*Timestamp: 271456, Event ID: 10006, Description: Response during non-trial period (arrow up)
Timestamp: 273907, Event ID: 10012, Description: Start of trial period (short increase)
Timestamp: 274146, Event ID: 10014, Description: Response
Timestamp: 276216, Event ID: 10016, Description: Start of trial period (long increase)
Timestamp: 276672, Event ID: 10018, Description: Response
Timestamp: 279055, Event ID: 10016, Description: Start of trial period (long increase)
Timestamp: 279570, Event ID: 10018, Description: Response
Timestamp: 281751, Event ID: 10016, Description: Start of trial period (long increase)
Timestamp: 282362, Event ID: 10018, Description: Response
Timestamp: 284651, Event ID: 10012, Description: Start of trial period (short increase)
Timestamp: 285396, Event ID: 10013, Description: Response
Weird period of response button presses, skipping to next volume event
Timestamp: 289103, Event ID: 10012, Description: Start of trial period (short increase)
Timestamp: 291602, Event ID: 10015, Description: End of trial period (no response, aka a miss)
Timestamp: 294651, Event ID: 10001, Description: Start of song playback
Timestamp: 300750, Event ID: 10007, Description: Start of trial period (long decrease)
Timestamp: 301606, Event ID: 10008, Description: Response
Timestamp: 303385, Event ID: 10012, Description: Start of trial period (short increase)
Timestamp: 303717, Event ID: 10014, Description: Response
Timestamp: 305890, Event ID: 10007, Description: Start of trial period (long decrease)
Timestamp: 306664, Event ID: 10008, Description: Response
Timestamp: 308957, Event ID: 10016, Description: Start of trial period (long increase)
Timestamp: 309459, Event ID: 10018, Description: Response
Timestamp: 311250, Event ID: 10002, Description: Start of trial period (short decrease)
Timestamp: 311434, Event ID: 10003, Description: Response
Timestamp: 313988, Event ID: 10002, Description: Start of trial period (short decrease)
Timestamp: 314298, Event ID: 10003, Description: Response
Timestamp: 316042, Event ID: 10007, Description: Start of trial period (long decrease)
Timestamp: 316509, Event ID: 10008, Description: Response
Timestamp: 319696, Event ID: 10007, Description: Start of trial period (long decrease)
Timestamp: 320199, Event ID: 10008, Description: Response
Timestamp: 323227, Event ID: 10007, Description: Start of trial period (long decrease)
Timestamp: 323779, Event ID: 10008, Description: Response
Timestamp: 326030, Event ID: 10002, Description: Start of trial period (short decrease)
Timestamp: 326341, Event ID: 10003, Description: Response
Timestamp: 328762, Event ID: 10007, Description: Start of trial period (long decrease)
Timestamp: 329757, Event ID: 10008, Description: Response
Timestamp: 331563, Event ID: 10012, Description: Start of trial period (short increase)
Timestamp: 331809, Event ID: 10014, Description: Response
Timestamp: 335040, Event ID: 10002, Description: Start of trial period (short decrease)
Timestamp: 335346, Event ID: 10004, Description: Response
Weird period of response button presses, skipping to next volume event
Timestamp: 337760, Event ID: 10007, Description: Start of trial period (long decrease)
Timestamp: 340263, Event ID: 10010, Description: End of trial period (no response, aka a miss)
Timestamp: 343389, Event ID: 10002, Description: Start of trial period (short decrease)
Timestamp: 345889, Event ID: 10005, Description: End of trial period (no response, aka a miss)
Timestamp: 349484, Event ID: 10001, Description: Start of song playback
*Timestamp: 353288, Event ID: 10011, Description: Response during non-trial period (arrow 
down)
Timestamp: 355806, Event ID: 10002, Description: Start of trial period (short decrease)
Timestamp: 356054, Event ID: 10003, Description: Response
Timestamp: 358673, Event ID: 10016, Description: Start of trial period (long increase)
Timestamp: 359401, Event ID: 10018, Description: Response
Timestamp: 362703, Event ID: 10016, Description: Start of trial period (long increase)
Timestamp: 362773, Event ID: 10018, Description: Response
*Timestamp: 364181, Event ID: 10011, Description: Response during non-trial period (arrow down)
Timestamp: 365792, Event ID: 10007, Description: Start of trial period (long decrease)
Timestamp: 366538, Event ID: 10008, Description: Response
Timestamp: 368546, Event ID: 10012, Description: Start of trial period (short increase)
Timestamp: 368945, Event ID: 10014, Description: Response
Timestamp: 371806, Event ID: 10012, Description: Start of trial period (short increase)
Timestamp: 372178, Event ID: 10014, Description: Response
*Timestamp: 374560, Event ID: 10006, Description: Response during non-trial period (arrow up)
Timestamp: 375306, Event ID: 10002, Description: Start of trial period (short decrease)
Timestamp: 375615, Event ID: 10003, Description: Response
Timestamp: 378165, Event ID: 10012, Description: Start of trial period (short increase)
Timestamp: 378690, Event ID: 10014, Description: Response
Timestamp: 382086, Event ID: 10012, Description: Start of trial period (short increase)
Timestamp: 382352, Event ID: 10014, Description: Response
Timestamp: 383906, Event ID: 10016, Description: Start of trial period (long increase)
Timestamp: 384259, Event ID: 10018, Description: Response
Timestamp: 386516, Event ID: 10016, Description: Start of trial period (long increase)
Timestamp: 387458, Event ID: 10018, Description: Response
Timestamp: 390838, Event ID: 10016, Description: Start of trial period (long increase)
Timestamp: 391652, Event ID: 10018, Description: Response
Timestamp: 394648, Event ID: 10016, Description: Start of trial period (long increase)
Timestamp: 395492, Event ID: 10018, Description: Response
Timestamp: 398692, Event ID: 10012, Description: Start of trial period (short increase)
Timestamp: 398992, Event ID: 10014, Description: Response
*Timestamp: 400437, Event ID: 10006, Description: Response during non-trial period (arrow up)
Timestamp: 401453, Event ID: 10016, Description: Start of trial period (long increase)
Timestamp: 401976, Event ID: 10017, Description: Response
Weird period of response button presses, skipping to next volume event
Timestamp: 407008, Event ID: 10016, Description: Start of trial period (long increase)
Timestamp: 409511, Event ID: 10019, Description: End of trial period (no response, aka a miss)
Timestamp: 413070, Event ID: 10001, Description: Start of song playback
*Timestamp: 415768, Event ID: 10011, Description: Response during non-trial period (arrow down)
Timestamp: 417847, Event ID: 10002, Description: Start of trial period (short decrease)
Timestamp: 418225, Event ID: 10003, Description: Response
Timestamp: 421406, Event ID: 10007, Description: Start of trial period (long decrease)
Timestamp: 422202, Event ID: 10008, Description: Response
Timestamp: 424928, Event ID: 10002, Description: Start of trial period (short decrease)
Timestamp: 425182, Event ID: 10003, Description: Response
Timestamp: 427541, Event ID: 10011, Description: Response during non-trial period (arrow down)
Timestamp: 428115, Event ID: 10016, Description: Start of trial period (long increase)
Timestamp: 429084, Event ID: 10018, Description: Response
Timestamp: 430842, Event ID: 10007, Description: Start of trial period (long decrease)
Timestamp: 431743, Event ID: 10008, Description: Response
Timestamp: 433495, Event ID: 10002, Description: Start of trial period (short decrease)
Timestamp: 433806, Event ID: 10003, Description: Response
Timestamp: 436684, Event ID: 10002, Description: Start of trial period (short decrease)
Timestamp: 436983, Event ID: 10003, Description: Response
Timestamp: 439429, Event ID: 10002, Description: Start of trial period (short decrease)
Timestamp: 439878, Event ID: 10003, Description: Response
Timestamp: 442036, Event ID: 10007, Description: Start of trial period (long decrease)
Timestamp: 442851, Event ID: 10008, Description: Response
Timestamp: 445459, Event ID: 10002, Description: Start of trial period (short decrease)
Timestamp: 445751, Event ID: 10003, Description: Response
Timestamp: 447736, Event ID: 10007, Description: Start of trial period (long decrease)
Timestamp: 448568, Event ID: 10008, Description: Response
Timestamp: 450474, Event ID: 10002, Description: Start of trial period (short decrease)
Timestamp: 450785, Event ID: 10003, Description: Response
Timestamp: 453479, Event ID: 10007, Description: Start of trial period (long decrease)
Timestamp: 454390, Event ID: 10008, Description: Response
Timestamp: 455404, Event ID: 10011, Description: Response during non-trial period (arrow down)
Timestamp: 457217, Event ID: 10002, Description: Start of trial period (short decrease)
Timestamp: 457515, Event ID: 10003, Description: Response
Timestamp: 459527, Event ID: 10002, Description: Start of trial period (short decrease)
Timestamp: 459804, Event ID: 10003, Description: Response
Timestamp: 461458, Event ID: 10002, Description: Start of trial period (short decrease)
Timestamp: 463958, Event ID: 10005, Description: End of trial period (no response, aka a miss)

"""

# Split the data into lines
lines = data.strip().split('\n')

# Initialize an empty list to store matching timestamps
matching_timestamps = []

# Iterate through each line and check for the specific description
for line in lines:
    if "Start of trial period" in line:
        # Extract the timestamp
        parts = line.split(',')
        timestamp = parts[0].split(': ')[1]  # Get the timestamp part
        matching_timestamps.append(timestamp)

# Convert timestamps to integers (in case they are strings)
matching_timestamps = [int(ts) for ts in matching_timestamps]

for timestamp in matching_timestamps:
    print(timestamp)
# # Initialize an empty list to store the cut intervals
# cut_intervals = []

# # Calculate cut intervals
# for timestamp in matching_timestamps:
#     start_time = timestamp - 100  # 10 ms before
#     end_time = timestamp + 250    # 100 ms after
#     cut_intervals.append((start_time, end_time))

# # Print the cut intervals
# print("Cut Intervals (Start, End):")
# for start, end in cut_intervals:
#     print(f"Start: {start} ms, End: {end} ms")