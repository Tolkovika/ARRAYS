distances_traveled = [120, 150, 180, 90, 200, 175, 160]
sorted_distances = sorted(distances_traveled)
print("Posortowane odległości (od najniższej do najwyższej):", sorted_distances)

daily_temperatures = [16, 17, 15, 14, 18, 19, 17, 15, 16, 18]
sorted_temperatures_desc = sorted(daily_temperatures, reverse=True)
print("Posortowane temperatury (od najwyższej do najniższej):", sorted_temperatures_desc)

file_names = ["report.docx", "presentation.pptx", "data.csv", "photo.jpg", "notes.txt",
   "invoice.pdf", "resume.docx", "budget.xlsx", "meeting.mp4", "schedule.pdf"]
sorted_file_names = sorted(file_names)
print("Posortowane nazwy plików (alfabetycznie):", sorted_file_names)
