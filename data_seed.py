BADGES_DATA = [
    {"name": "Ninja Graduate", "desc": "Completed a Naruto quiz!", "icon": "user-ninja"},
    {"name": "Pirate Recruit", "desc": "Joined the Grand Line Arena!", "icon": "ship"},
    {"name": "Titan Slayer", "desc": "Mastered the AOT trivia!", "icon": "khanda"},
    {"name": "First Blood", "desc": "Scored 100% on any quiz!", "icon": "fire"},
    {"name": "Quiz Master", "desc": "Completed a 20-question challenge!", "icon": "brain"},
    {"name": "Anime Sage", "desc": "Reached Level 10!", "icon": "scroll"}
]

ROOMS_DATA = [
    {"name": "Hidden Leaf Village", "anime": "Naruto", "desc": "20-Question Elite Shinobi Exam.", "img": "https://images.unsplash.com/photo-1578632738981-43c94101e912?q=80&w=400"},
    {"name": "The Grand Line", "anime": "One Piece", "desc": "20-Question Pirate King Challenge.", "img": "https://images.unsplash.com/photo-1607604276583-eef5d076aa5f?q=80&w=400"},
    {"name": "Shiganshina District", "anime": "Attack on Titan", "desc": "20-Question Survey Corps Trial.", "img": "https://images.unsplash.com/photo-1541562232579-512a21360020?q=80&w=1200"}
]

NARUTO_QUESTIONS = [
    ("Who was the creator of the Reaper Death Seal?", [("The Uzumaki Clan", True), ("Minato", False), ("Senju", False), ("Hashirama", False)]),
    ("What is the name of the monk guarding the Fire Temple?", [("Chiriku", True), ("Asuma", False), ("Hidan", False), ("Konohamaru", False)]),
    ("How many hearts did Kakuzu have?", [("5", True), ("4", False), ("3", False), ("6", False)]),
    ("Who was the leader of the Akatsuki before Nagato?", [("Yahiko", True), ("Obito", False), ("Madara", False), ("Konan", False)]),
    ("What animal is summoned by Tsunade?", [("Slug", True), ("Snail", False), ("Toad", False), ("Snake", False)]),
    ("Which clan does Karin belong to?", [("Uzumaki", True), ("Uchiha", False), ("Hyuga", False), ("Inuzuka", False)]),
    ("Who is the father of Kakashi?", [("Sakumo Hatake", True), ("Might Duy", False), ("Minato", False), ("Tobirama", False)]),
    ("What is the name of Neji's forehead seal?", [("Caged Bird", True), ("Heaven's Seal", False), ("Death Seal", False), ("Mark of Cain", False)]),
    ("What move did Naruto use to defeat Kaguya?", [("Reverse Harem", True), ("Rasengan", False), ("Chidori", False), ("Sage Art", False)]),
    ("What is the village hidden in the rain?", [("Amegakure", True), ("Konoha", False), ("Suna", False), ("Kiri", False)]),
    ("What sword does Kisame use?", [("Samehada", True), ("Kubikiribocho", False), ("Hiramekarei", False), ("Kiba", False)]),
    ("Who taught Jiraiya Sage Mode?", [("Great Toad Sage", True), ("Minato", False), ("Naruto", False), ("Third Hokage", False)]),
    ("What forbidden jutsu does Might Guy use?", [("Eight Gates", True), ("Reanimation", False), ("Shadow Clone", False), ("Susanoo", False)]),
    ("Who was the 2nd Tsuchikage?", [("Mu", True), ("Onoki", False), ("Deidara", False), ("Gaara", False)]),
    ("What is the name of the bridge where Haku died?", [("Great Naruto Bridge", True), ("Hidden Mist Bridge", False), ("Samurai Bridge", False), ("Leaf Bridge", False)]),
    ("Which member used the Hiramekarei?", [("Chojuro", True), ("Zabuza", False), ("Raiga", False), ("Mangetsu", False)]),
    ("What was Sasori's first human puppet?", [("Komushi", True), ("3rd Kazekage", False), ("Hiruko", False), ("Sakura", False)]),
    ("Who called Naruto 'Bozuzu'?", [("Gamakichi", True), ("Kurama", False), ("Killer Bee", False), ("Iruka", False)]),
    ("What flute does Tayuya use?", [("Demon Flute", True), ("Ghost Flute", False), ("Bone Flute", False), ("Wind Flute", False)]),
    ("How many tails did Naruto have against Pain?", [("6 and 8", True), ("4", False), ("9", False), ("1", False)])
]

ONE_PIECE_QUESTIONS = [
    ("What island were Poneglyphs created on?", [("Wano", True), ("Ohara", False), ("Laugh Tale", False), ("Zou", False)]),
    ("Who first wounded Kaido?", [("Kozuki Oden", True), ("Garp", False), ("Shanks", False), ("Whitebeard", False)]),
    ("What was Robin's bounty at age 8?", [("79 Million", True), ("80 Million", False), ("100 Million", False), ("50 Million", False)]),
    ("What is Luffy's father's name?", [("Monkey D. Dragon", True), ("Monkey D. Garp", False), ("Gol D. Roger", False), ("Sabo", False)]),
    ("Who is the archaeologist of the crew?", [("Nico Robin", True), ("Nami", False), ("Usopp", False), ("Brook", False)]),
    ("What fruit did Ace eat?", [("Mera Mera", True), ("Gomu Gomu", False), ("Hito Hito", False), ("Magu Magu", False)]),
    ("What is Zoro's ultimate goal?", [("Strongest Swordsman", True), ("Find One Piece", False), ("Kill Kaido", False), ("Protect Luffy", False)]),
    ("What is the name of Luffy's ship?", [("Thousand Sunny", True), ("Going Merry", False), ("Oro Jackson", False), ("Moby Dick", False)]),
    ("Who gave Luffy his straw hat?", [("Shanks", True), ("Roger", False), ("Garp", False), ("Dragon", False)]),
    ("What is Sanji's dream?", [("All Blue", True), ("Cook for King", False), ("Beat Zeff", False), ("Find Nami", False)]),
    ("Who was the first crew member?", [("Zoro", True), ("Nami", False), ("Usopp", False), ("Sanji", False)]),
    ("What is Brook's fruit?", [("Yomi Yomi", True), ("Hana Hana", False), ("Gomu Gomu", False), ("Kage Kage", False)]),
    ("Who is the King of the Pirates?", [("Gol D. Roger", True), ("Whitebeard", False), ("Kaido", False), ("Luffy", False)]),
    ("What is the name of the desert kingdom?", [("Alabasta", True), ("Wano", False), ("Dressrosa", False), ("Skypiea", False)]),
    ("Who is the captain of the Heart Pirates?", [("Trafalgar Law", True), ("Kid", False), ("Killer", False), ("Bepo", False)]),
    ("What is the highest bounty ever?", [("Roger's", True), ("Whitebeard's", False), ("Luffy's", False), ("Kaido's", False)]),
    ("Who is the doctor of the crew?", [("Tony Tony Chopper", True), ("Law", False), ("Marco", False), ("Crocus", False)]),
    ("What is Franky's real name?", [("Cutty Flam", True), ("Franky", False), ("Iceburg", False), ("Tom", False)]),
    ("What is Jinbe's title?", [("First Knight of the Sea", True), ("Warlord", False), ("Yonko", False), ("Revolutionary", False)]),
    ("Where was Sanji born?", [("North Blue", True), ("East Blue", False), ("South Blue", False), ("West Blue", False)])
]

AOT_QUESTIONS = [
    ("Who first inherited the Founding Titan?", [("Maria Fritz", True), ("Rose", False), ("Sina", False), ("Karl", False)]),
    ("What chemical turns Eldians into Titans?", [("Spinal Fluid", True), ("Serum", False), ("Extract", False), ("Blood", False)]),
    ("Who is the protagonist?", [("Eren Yeager", True), ("Levi", False), ("Mikasa", False), ("Armin", False)]),
    ("What is inside the Walls?", [("Colossal Titans", True), ("Gold", False), ("Humans", False), ("Nothing", False)]),
    ("Who was the 145th King?", [("Karl Fritz", True), ("Uri Reiss", False), ("Rod Reiss", False), ("Eren", False)]),
    ("What is the name of the beast titan?", [("Zeke Yeager", True), ("Reiner", False), ("Bertholdt", False), ("Annie", False)]),
    ("Who killed the Beast Titan?", [("Levi Ackerman", True), ("Eren", False), ("Erwin", False), ("Mikasa", False)]),
    ("What is the name of the harbor city?", [("Liberio", True), ("Shiganshina", False), ("Trost", False), ("Stohess", False)]),
    ("What is the name of the scouting group?", [("Survey Corps", True), ("Garrison", False), ("Military Police", False), ("Cadets", False)]),
    ("Who wrote the letter to Historia?", [("Ymir", True), ("Reiner", False), ("Eren", False), ("Bertholdt", False)]),
    ("What is the name of Eren's titan?", [("Attack Titan", True), ("Founding Titan", False), ("War Hammer", False), ("Armor", False)]),
    ("Who is the Female Titan?", [("Annie Leonhart", True), ("Mikasa", False), ("Historia", False), ("Pieck", False)]),
    ("What is the title of the first episode?", [("To You, 2,000 Years From Now", True), ("The Fall", False), ("Hope", False), ("The Wall", False)]),
    ("Who is the commander before Hange?", [("Erwin Smith", True), ("Keith", False), ("Pixis", False), ("Nile", False)]),
    ("What is the true identity of the Titans?", [("Eldians", True), ("Marleyans", False), ("Aliens", False), ("Demons", False)]),
    ("Who is the Jaw Titan after Ymir?", [("Falco Grice", True), ("Porco", False), ("Marcel", False), ("Annie", False)]),
    ("What is the name of the sea?", [("Ocean", True), ("River", False), ("Blue", False), ("Grand Line", False)]),
    ("What is the secret in Eren's basement?", [("The Truth of the World", True), ("Titan Serum", False), ("Gold", False), ("A Diary", False)]),
    ("Who is the Cart Titan?", [("Pieck Finger", True), ("Annie", False), ("Gabi", False), ("Zeke", False)]),
    ("What is the final plan of Eren?", [("The Rumbling", True), ("Peace", False), ("Escape", False), ("Death", False)])
]
