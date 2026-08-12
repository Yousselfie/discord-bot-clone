import glob, json

my_messages = []

#Getting all of the text messages
for path in glob.glob("discord_export/messages/*/messages.json"): #traverse through the folder of jsonified discord messages
    with open(path, encoding="utf-8") as f:
        for msg in json.load(f): #for one element(line) of the messages.json file
            msg_year = int(msg.get("Timestamp", "").strip()[:4]) #Get the year of the message timestamp and convert to int
            if msg_year >= 2023: #I don't want any messages before 2023
                text = msg.get("Contents", "").strip() #Get the actual text message
                if text and not text.startswith("http") and text[0].isalpha(): #Ensure the text exists, starts with a letter, and try to avoid bare links
                    my_messages.append(text)


#Keep a sample of decent length messages
sample = [m for m in my_messages if 3 < len(m) < 200][:300]
with open ("style_example.txt", "w", encoding="utf-8") as f: #Write sample to text file
    f.write("\n".join(sample))

print(f"Saved {len(sample)} example messages")