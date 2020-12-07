import random
from nltk.corpus import brown


COMMON_PHRASES = [
    "A bird in the hand is worth two in the bush.",
    "A penny for your thoughts.",
    "A penny saved is a penny earned.",
    "A picture is worth 1000 words.",
    "Actions speak louder than words.",
    "Barking up the wrong tree.",
    "Birds of a feather flock together.",
    "By the skin of your teeth.",
    "Comparing apples to oranges.",
    "Do unto others as you would have them do unto you.",
    "Don't count your chickens before they hatch.",
    "Don't cry over spilt milk.",
    "Don't give up your day job.",
    "Don't put all your eggs in one basket.",
    "Every cloud has a silver lining.",
    "Get a taste of your own medicine.",
    "Good things come to those who wait.",
    "He has bigger fish to fry.",
    "He's a chip off the old block.",
    "Hit the nail on the head.",
    "It ain't over till the fat lady sings.",
    "It takes one to know one.",
    "It's raining cats and dogs.",
    "Kill two birds with one stone.",
    "Let the cat out of the bag.",
    "Look before you leap.",
    "Saving for a rainy day.",
    "Slow and steady wins the race.",
    "Take it with a grain of salt.",
    "The ball is in your court.",
    "The best thing since sliced bread.",
    "The devil is in the details.",
    "The early bird gets the worm.",
    "The elephant in the room.",
    "The whole nine yards.",
    "There are other fish in the sea.",
    "There's a method to his madness.",
    "There's no such thing as a free lunch.",
    "Throw caution to the wind.",
    "You can't have your cake and eat it too.",
    "You can't judge a book by its cover.",
    "A little learning is a dangerous thing.",
    "A snowball's chance in hell.",
    "A stitch in time saves nine.",
    "An apple a day keeps the doctor away.",
    "An ounce of prevention is worth a pound of cure.",
    "Bolt from the blue.",
    "Calm before the storm.",
    "Curiosity killed the cat.",
    "Don't beat a dead horse.",
    "Every dog has his day.",
    "Familiarity breeds contempt.",
    "Fortune favours the bold.",
    "Haste makes waste.",
    "He who laughs last laughs loudest.",
    "He's not playing with a full deck.",
    "He's sitting on the fence.",
    "It is a poor workman who blames his tools.",
    "It is always darkest before the dawn.",
    "It takes two to tango.",
    "Know which way the wind is blowing.",
    "Leave no stone unturned.",
    "Let sleeping dogs lie.",
    "Like riding a bicycle.",
    "Like two peas in a pod.",
    "Make hay while the sun shines.",
    "Once bitten, twice shy.",
    "Out of the frying pan and into the fire.",
    "Shape up or ship out.",
    "The pot calling the kettle black.",
    "There are clouds on the horizon.",
    "Those who live in glass houses shouldn't throw stones.",
    "Through thick and thin.",
    "Waste not, want not.",
    "Well begun is half done.",
    "When it rains it pours.",
    "You can't make an omelet without breaking some eggs.",
]

FACTS = [
    "There are more possible iterations of a game of chess than there are atoms in the known universe. There are also more ways to arrange a deck of cards than atoms in the known universe.",
    "Cleopatra lived closer in time to the Moon landing than to the construction of the Great Pyramid of Giza.",
    "It can take a photon 40,000 years to travel from the core of the sun to the surface, but only 8 minutes to travel the rest of the way to earth.",
    "It would take 1,200,000 mosquitoes, each sucking once, to completely drain the average human of blood.",
    "Written language was invented independently by the Egyptians, Sumerians, Chinese, and Mayans.",
    "If you were to remove all of the empty space from the atoms that make up every human on earth, the entire world population could fit into an apple. ",
    "Honey does not spoil. You could feasibly eat 3000 year old honey. It does, however, crystallise with time, but all you have to do is put it in water and warm it until it’s back to its original state and you can eat it.",
    "If you somehow found a way to extract all of the gold from the bubbling core of our lovely little planet, you would be able to cover all of the land in a layer of gold up to your knees.",
    "To know when to mate, a male giraffe will continuously headbutt the female in the bladder until she urinates. The male then tastes the pee and that helps it determine whether the female is ovulating.",
    "The largest known living organism is an aspen grove. Pando (Latin for I spread out) is a group of genetically identical quaking aspens in Utah with an interconnected root system. It's an estimated 80,000 years old and takes up more than 400000 m2.",
    "You can hear a blue whale's heartbeat from more than 2 miles away. The world's largest animal's heart weighs about 180kg - approximately the size of a small piano.",
    "Four times more people speak English as a second language than as a native one. It's the most widely spoken tongue in the world, with nearly two billion people learning it as a second language and only 350 million people speaking it natively.",
    "About 700 grapes go into one bottle of wine. That's approximately 1.2kg per bottle.",
    "Armadillo shells are bulletproof. In fact, one Texas man was hospitalized when a bullet he shot at an armadillo ricocheted off the animal and hit him in the jaw.",
    "Chess is called the game of kings. It has been around for over 500 years and is based on an even older game from India. The chess played today is from Europe.",
    "It might seem safe to assume that the Canary Islands were named after canary birds, but the location was actually named after dogs. Although it's off the coast of northwestern Africa, the archipelago is actually part of Spain. In Spanish, the area's name is Islas Canarias, which comes from the Latin phrase 'Canariae Insulae' which means 'island of dogs.'",
    "When 174 world leaders signed the Paris Agreement on Earth Day in 2016 at the United Nations (UN) headquarters in New York, it was the largest number of countries ever to come together to sign anything on a single day, according to the UN. The agreement aimed to combat climate change and accelerate and intensify the actions and investments needed to strengthen the global climate effort.",
    "Earthquakes can range from minor tremors that are barely noticeable to building-toppling ground-shakers that cause massive destruction. But it's an inevitable part of life for those who live in countries such as China, Indonesia, Iran, and Turkey, which are some of the most earthquake-prone places on the planet. However, according to the U.S. Geological Survey, Japan records the most earthquakes in the world.",
    "According to the Population Reference Bureau, since the time Homo sapiens first hit the scene 50,000 years ago, more than 108 billion members of our species have been born. And a large chunk of that number is alive right now. According to the bureau, the number of people alive today represents a whopping seven percent of the total number of humans who have ever lived.",
    "Not everyone lives in a booming city or sprawling suburb. Many people still make their homes outside of bustling locations-especially in India, which has the largest number of people living in rural areas (approximately 893 million people live outside of the city), according to Reuters. China also has an impressively large rural population, with 578 million living outside of major centers.",
    "Some countries are hundreds of years old, while others can trace their nation's history back for thousands of years. But South Sudan in North Africa just gained its independence from Sudan in 2011, which currently makes it the youngest country in the world.",
    "The British royal family may be the most famous royal family on the planet, but there are still plenty of other nobles out there. In total, there are 28 royal families who rule over a total of 43 countries around the world, including Japan, Spain, Swaziland, Bhutan, Thailand, Monaco, Sweden, the Netherlands, and Liechtenstein.",
    "The panda at your local zoo may look like it's at home in its cozy sanctuary. But unless you live in China, the pandas that you're seeing are just visiting. That's because every one of the gentle giants in zoos around the world are on loan from China. Yes, they're technically the property of the government of China.",
    "During his lifetime between 1162 and 1227, Genghis Khan fathered countless children. And while we may never know exactly how many offspring the leader of the Mongol Empire had, scientists now believe that around 1 in every 200 men- around 16 million people-are direct descendants of his, according to a 2003 historical genetics paper.",
    "Tokyo is a booming city-not only by Japanese standards, but also compared to cities around the world. With around 37 million people living in Tokyo, it's the world's largest city when it comes to population size, according to Reuters. The next largest city is Delhi, India, (population 29 million) and Shanghai, China (population 26 million).",
    "Canadians say 'sorry' so much that a law was passed in 2009 declaring that an apology can't be used as evidence of admission to guilt.",
    "Back when dinosaurs existed, there used to be volcanoes that were erupting on the moon.",
    "There were two AI chatbots created by Facebook to talk to each other, but they were shut down after they started communicating in a language they made for themselves.",
    "In 2009, Stephen Hawking held a reception for time travelers, but didn't publicize it until after. This way, only those who could time travel would be able to attend. Nobody else attended.",
    "In World War II, Germany tried to collapse the British economy by dropping millions of counterfeit bills over London.",
    "Birds are the closest living relatives of crocodilians, as well as the descendants of extinct dinosaurs with feathers. This makes them the only surviving dinosaurs.",
    "Cold showers have more health benefits than hot or warm showers. These include improving circulation, stimulating weight loss, and easing depression.",
    "During the first live iPhone presentation, Steve Jobs had to frequently switch phones behind his desk. Otherwise, it would run out of RAM and crash.",
    "Movie theaters make roughly 85 percent of their profit off concession stands. This is because ticket revenues have to be shared with the movie distributors.",
    "If you ate nothing but rabbit meat, you would die from protein poisoning. This would be a mixture of too much protein and an absence of fat in the diet.",
    "Italy built an entire courthouse to prosecute the Mafia. They charged 474 members in a trial that lasted from 1986-1992. To date, it was the biggest trial in the world.",
    "Pitbulls rank high among the most affectionate and least aggressive dogs. Pitbulls are only aggressive when forcibly trained as such; usually for illegal dog fighting.",
    "When Blackbeard captured ships, many of the African slaves on board would go on to become pirates. When he died, nearly one-third of his total crew were former slaves.",
    "Cucumber can actually cure bad breath. A slice pressed to the roof of your mouth for 30 seconds with your tongue allows the phytochemicals to kill the problematic bacteria.",
    "The King of Macedon threatened Sparta with 'If I bring my army into your land, I will raze your city'. The Spartans replied: 'If'. No attempt was made to capture the city.",
    "Einstein's brain went missing when he died in 1955 and was lost for 23 years. The doctor who worked on his autopsy stole it and kept in a hidden cider box.",
    "The costume designers for The Lord of the Rings worked for two straight years making custom armor. Just one Orc suit had 13,000 rings and took 3 days to make.",
    "Mulan has the highest kill-count of any Disney character, including villains, and was the first Disney Princess to be shown killing people on-screen.",
    "One of the earliest depictions of dreadlocks dates back to 1600 BC to the Minoan Civilization, one of Europe's earliest civilizations, who lived in what is now known as Greece.",
    "The reason the taste of artificial banana flavoring and artificial banana flavored products doesn't taste like bananas is because it is based on a type of banana that was wiped out by a plague in the 1950's.",
    "Due to the humid and moist conditions that a sloth lives in, moss and other similar plants will sometimes grow in its hair. Sloths also have very bad eyesight. These two factors can sometimes culminate in a sloth grabbing its own arm, whilst thinking it is a branch, and falling to its death!",
    "American microbiologist Maurice Ralph Hilleman is accredited with developing 8 of the 14 routine vaccinations used today, these being; Measles, Mumps, Hepatitis A & B, Chickenpox, Meningitis, Pneumonia, and Hemophilia influenza. He also discovered that Chlamydia was not a virus as it was previously thought to be.",
    "It is predicted that the reason why night insects, such as moths, are attracted to lights is because they mistake them for the light of the moon, which they used to navigate the Earth before mankind made artificial lights.",
    "Film producer Jeffrey Katzenberg revived The Walt Disney Studios by producing some of their biggest hits: The Little Mermaid, The Lion King, Beauty and the Beast and Aladdin. After these he requested a promotion, and was then abruptly fired by them. He then swore revenge against Disney and founded DreamWorks Studios.",
    "Through the use of optogenetics, scientists were able to create a false memory within a mouse's brain. This was done by marking the neurons that fired in the mouse's brain when in one environment, transferring the mouse to a second environment and making these neurons fire whilst shocking the mouse's feet, then transferring the mouse back to the first environment. This made the mouse believe it had had an unpleasant experience in the first environment when in fact it hadn't.",
    "The word 'quarantine' derives from the Venetian dialect of Italian and the words 'quaranta giorni', meaning 'forty days'. This is because when it was discovered that ships were infested with plague-carrying rats they were made to sit at anchor outside Venice's city walls for forty days before coming ashore.",
    "In a survival situation if you were to drink seawater it would rapidly dehydrate you and soon lead to your death. However, it is vastly less harmful to eat frozen seawater. This is because it contains a tenth the amount of salt as its liquid form, due to the fact that the salt is separated from the water when freezing as it does not fit into the crystalline structure of ice.",
    "Due to the extremely warm weather in the summer of 2013, several nuclear power plants across the world, including ones in Japan, Israel and Scotland, were forced to close down because of a sudden increase in the population of Jellyfish. The mass amounts of Jellyfish clogged the filters that draw seawater into the power plants in order to cool down their reactors!",
    "France has conducted 210 nuclear weapon tests, more than the United Kingdom, China, India, and North Korea combined! This is scarcely a fifth of the amount conducted by the United States, however, who have conducted roughly 1,054 tests.",
    "Iran carries out more gender-change operations than any other country in the world. According to official statistics Iran has somewhere between 15,000 and 20,000 transsexuals inhabiting it, although unofficial statistics place that number at approximately 150,000!",
    "There is an Australian man, James Harrison, who has a singularly unique blood plasma composition that has been used to cure Rhesus disease, a hemolytic disease that affects newborn babies. He has donated his blood plasma over 1000 times.",
    "In Bordeaux, France, 1940, Portuguese diplomat Aristides de Sousa Mendes issued an estimated 30,000 Portuguese travel visas in order to Jewish families flee persecution from the Nazis. Once his superiors had learned of his actions, he was ordered back to Portugal, dismissed from office and denied his pension benefits. Sousa Mendes went on to die in 1954, impoverished and unsung.",
    "Archeologists in London have found a Mesolithic tool-making factory that gives substantial proof human beings were living on the River Thames 7,000 B.C. That's over 9,000 years ago!",
    "In 1995, strange 7-foot circular patterns were discovered on the ocean's floor. Deemed the 'crop circles of the sea', these mysterious patterns went unanswered for until early 2011 when it was discovered that 5-inch long male puffer-fish were the culprits. After studying these animals, scientists have discovered that the meticulous creation and upkeep of these patterns by the puffer-fish serve as an attraction for the opposite sex as well as a nest for the female puffer-fish's eggs.",
    "In the bioengineering department of the University of Illinois, researchers have created small ‘biobots’, partly out of synthetic gel and partly out of muscle cell, that can move on their own. Whilst only a small scientific step, this is the building blocks for ‘nanotechnology’: tiny devices that could exist within the human body, freely detecting illness and administering medication.",
    "Colombian drug-lord Pablo Escobar kept four Hippos in his estate before his death in 1993. Deemed too much hassle to move by authorities, his Hippos were left there and have since bred and escaped becoming an invasive species of Colombia.",
    "The world's biggest tire producer is LEGO. In 2011, LEGO manufactured over 318 million tires, while brands such as Bridgestone, Michelin, Goodyear all produced below 200 million each. In Billund, Denmark, LEGO produces 870,000 tyres every day. They may be tiny toy tires, but the fact still stands.",
    "Research has found that a mid-day nap can make you more creative, focused, and fresh for the rest of the day. But one study also found that they can also reduce your risk of heart attack. Specifically, those who regularly nap were found to be 37 percent less likely to die from a heart attack or other coronary ailment than those who worked straight through the day.",
    "Dolphins sometimes play with Orcas, even though some Orcas eat Dolphins. Researchers believe this is because Orcas that eat red meat tend to avoid Orcas that only eat fish, so if they stay near the fish-eaters, they won’t encounter the mammal-eaters.",
    "Landing humans on the Moon required the most sudden burst of technological creativity and the largest commitment of resources ever made by any nation in peacetime. At its peak, the Apollo program employed 400,000 people and required the support of over 20,000 industrial firms and universities.",
    "There are more life forms on human skin than there are people on our planet. Every day we share our body with 90 trillion bacteria.",
    "The possibility of dying on your way to buy a lottery ticket is higher than the possibility of actually winning the lottery. You are also more likely to be struck by lightning in your lifetime than than win the lottery.",
    "Pessimism is inherited genetically. People who think negatively often have a mutated ADRA2b gene.",
    "In 1913, upon Edinburgh Zoo's opening, Norway gifted them their first king penguin. Since 1972, the Norwegian King's Guard has adopted 3 penguins, at differrent time periods, and each was given a rank within the regiment. One of them was even knighted by King Harald V of Norway as Sir Nils Olav III",
    "While the Egyptians were building the pyramids, a colony of Woolly mammoths that had survived, took residence on a small island called Wrangle Island. Mammoths lived there up until around 1,650 BCE, which is nearly 1,000 years after the pyramids were built.",
    "Jack Black is the son of rocket scientists. His parents, Thomas William Black and Judith Love Cohen were satellite engineers who worked on the Hubble Space Telescope.",
    "Ethan Zuckerman invented popup ads in the late 90s while working for Tripod.com. He has since apologized for inventing the most annoying internet tool in history.",
    "Green is seen as a symbol of life, but scientists claim that the earliest life on Earth might have been purple. Currently, chlorophyll molecules create the greenish hue of organisms. However, scientists theorize that ancient microbes may have used a different molecule to harness sun rays, giving organisms a violet hue instead.",
    "The Earth is not a perfect sphere: instead, it is an oblate spheroid. Scientists discovered that the Earth has a different size towards the equator. Back then, it was slimmer towards the equator and larger towards the North and South poles. However, they recently observed that the Earth has been bulging at the equator. Global warming is cited as the main factor, since the glacier melting redistributes oceanic mass throughout the planet.",
    "Nowadays, E-commerce is a dominant market. Who wouldn’t want to get anything at the click of a button? However, you’d be surprised that the earliest sale transaction on the internet was of weed. Recorded in the 1970s, the stash was negotiated between Stanford and MIT students.",
    "Walmart once had over 23,000 applications for 600 jobs in D.C. With those numbers, the Walmart acceptance rate was at 2.6%. This makes it twice as hard as getting into Harvard and over five times harder than getting into Cornell.",
    "According to the UNESCO World Happiness Report of 2019, Finland has been the world’s happiest country for 2 consecutive years. The data is based on citizens asked to rate their life from 1 to 10. Interestingly, Finland is closely followed by other European countries such as Denmark, Norway, Iceland, and the Netherlands.",
    r"According to a 2014 study, 12 out of 15 addicts were able to quit smoking through magic mushrooms. For 3 sessions, the chronic smokers were treated with psychedelic mushrooms. Surprisingly, the 80% success rate dwarfed the 35% success rate of leading treatment drugs.",
    "Every year, the town of Lopburi holds a buffet for monkeys. During the Monkey Buffet Festival, the town serves 3000 kgs of fruits and vegetables for local monkeys to enjoy.",
    "Rowan Atkinson has made generations laugh at his goofy antics as Mr. Bean. However, the Englishman is actually quite the intellectual. What most people don’t know is that Atkinson has a Master’s degree in Electrical Engineering from Oxford up his sleeve.",
    "Chlorine is in all of our bodily secretions and excretions. Our body’s chlorine levels are almost always parallel to the levels of sodium (due to the makeup of salt i.e. sodium chloride). There is enough chlorine in the body to disinfect five swimming pools.",
    "Adrenaline is a hormone released by our body during stressful situations. This hormone gives us a temporary boost of strength, speed, or basically anything that can help us stay alive. In some cases, adrenaline also keeps us from feeling the pain of fatal wounds. ",
    r"The Sun accounts for 99.86% of the mass in our solar system with a mass of around 330,000 times that of Earth. The Sun is made up of mostly hydrogen (three quarters worth) with the rest of its mass attributed to helium.",
    "The universe extends far beyond our own galaxy, The Milky Way, which is why scientists can only estimate how many stars are in space.  However, scientists estimate the universe contains approximately 1 septillion (1 followed by 24 zeros!) stars. While no one can actually count every single grain of sand on the earth, the estimated total from researchers at the University of Hawaii, is somewhere around seven quintillion, so there are many more stars in the known universe than grains of sand on Earth.",
    r"In Monopoly, when a player throws doubles (both dice land on the same number) he may take another turn. However, if he throws doubles three times in one turn, then he is considered to be 'speeding' and must go to jail. There is an approximately 0.46% chance of this happening. However, a monopoly game lasts about 20-25 turns, so according to Wolfram Alpha that's about a 7% chance of rolling three doubles in the whole game.",
]

NOVEL_EXCERPTS = [
    "The Ministry of Truth, which concerned itself with news, entertainment, education and the fine arts. The Ministry of Peace, which concerned itself with war. The Ministry of Love, which maintained law and order. And the Ministry of Plenty, which was responsible for economic affairs. Their names, in Newspeak: Minitrue, Minipax, Miniluv and Miniplenty.",
    "He found himself understanding the wearisomeness of this life, where every path was an improvisation and a considerable part of one's waking life was spent watching one's feet.",
    "Vonnegut could not help looking back, despite the danger of being turned metaphorically into a pillar of salt, into an emblem of the death that comes to those who cannot let go of the past.",
    "But I remembered one thing: it wasn't me that started acting deaf; it was people that first started acting like I was too dumb to hear or see or say anything at all.",
    "When today fails to offer the justification for hope, tomorrow becomes the only grail worth pursuing.",
    "It is far better to endure patiently a smart which nobody feels but yourself, than to commit a hasty action whose evil consequences will extend to all connected with you; and besides, the Bible bids us return good for evil.",
    "As I took another breath, I saw the three stars again. They were not calling to me; they were letting me go, leaving me to the black universe I had wandered for so many lifetimes. I drifted into the black, and it got brighter and brighter. It wasn't black at all-it was blue. Warm, vibrant, brilliant blue... I floated into it with no fear at all.",
    "Religion is like language or dress. We gravitate toward the practices with which we were raised. In the end, though, we are all proclaiming the same thing. That life has meaning. That we are grateful for the power that created us.",
    "First, let no one rule your mind or body. Take special care that your thoughts remain unfettered... Give men your ear, but not your heart. Show respect for those in power, but don't follow them blindly. Judge with logic and reason, but comment not. Consider none your superior whatever their rank or station in life. Treat all fairly, or they will seek revenge. Be careful with your money. Hold fast to your beliefs and others will listen.",
    "Love, whether newly born or aroused from a deathlike slumber, must always create sunshine, filling the heart so full of radiance, that it overflows upon the outward world.",
    "You're both the fire and the water that extinguishes it. You're the narrator, the protagonist, and the sidekick. You're the storyteller and the story told. You are somebody's something, but you are also your you.",
    "When you cannot pinpoint a pain in your body, the whole world seems to throb with it. Trees in pain, lit windows in pain, Wednesday nights in pain. Pianos flaming with pain, and the scale sliding up into a cry.",
    "At an early age, I learned that people make mistakes, and you have to decide if their mistakes are bigger than your love for them.",
    "Grief was what you owed the dead for the necessary crime of living on without them.",
    "If you are one of those people who has the ability to make it down to the bottom of the ocean, the ability to swim the dark waters without fear, the astonishing ability to move through life's worst crucibles and not die, then you also have the ability to bring something back to the surface that helps others in a way that they cannot achieve themselves.",
    "Her life is architected, elegant and angular, a beauty to behold, and mine is a stew, a juicy, sloppy mess of ingredients and feelings and emotions, too much salt and spice, too much anxiety, always a little dribbling down the front of my shirt. But have you tasted it? It's delicious.",
    "I kept thinking about the uneven quality of time - the way it was almost always so empty, and then with no warning came a few days that felt so dense and alive and real that it seemed indisputable that that was what life was, that its real nature had finally been revealed.",
    "Mother died today. Or maybe yesterday, I don't know. I had a telegram from the home: 'Mother passed away. Funeral tomorrow. Yours sincerely.' That doesn't mean anything. It may have been yesterday.",
    "America was never innocent. We popped our cherry on the boat over and looked back with no regrets. You can't ascribe our fall from grace to any single event or set of circumstances. You can't lose what you lacked at conception.",
    "The studio was filled with the rich odour of roses, and when the light summer wind stirred amidst the trees of the garden, there came through the open door the heavy scent of the lilac, or the more delicate perfume of the pink-flowering thorn.",
    "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
    "I was 37 then, strapped in my seat as the huge 747 plunged through dense cloud cover on approach to Hamburg Airport. Cold November rains drenched the earth. lending everything the gloomy air of a Flemish landscape: the ground crew in waterproofs, a flag atop a squat building, a BMW billboard. So - Germany again.",
    "Nikki, the name we finally gave my younger daughter, is not an abbreviation; it was a compromise I reached with her father. For paradoxically it was he who wanted to give her a Japanese name and I - perhaps out of some selfish desire not to be reminded of the past - insisted on an English one.",
    "Her first name was India - she was never able to get used to it. It seemed to her that her parents must have been thinking of someone else when they named her. Or were they hoping for another sort of daughter? As a child she was often on the point of inquiring, but time passed, and she never did.",
    "For seven years I tried not to remember too much because there was too much to remember, and I didn't want to fall any further behind with the events of my life. I still don't have a vegetable garden. I still haven't been to France. I have gone to bed with enough people that they seem like actual people now, but while I was going to bed with them I thought I was catching up. I am sorry. I had lost what seemed like a lot of time.",
    "Nobody died that year. Nobody prospered. There were no births or marriages. Seventeen reverent satires were written - disrupting a cliche and, presumably, creating a genre. There was a dream, of course, but many of the most important things, I find, are the ones learned in your sleep. Speech, tennis, music, skiing, manners, love - you try them waking and perhaps balk at the jump, and then you're over.",
    "You don't know about me, without you have read a book by the name of The Adventures of Tom Sawyer, but that ain't no matter. That book was made by Mr Mark Twain, and he told the truth, mainly. There was things he stretched, but mainly he told the truth. That is nothing.",
    "It's funny. Don't ever tell anybody anything. If you do, you start missing everybody.",
    "He was soon borne away by the waves, and lost in darkness and distance.",
    "So we beat on, boats against the current, borne back ceaselessly into the past.",
    "There was a white horse, on a quiet winter morning when snow covered the streets gently and was not deep, and the sky was swept with vibrant stars, except in the east, where dawn was beginning in a light blue flood. The air was motionless, but would soon start to move as the sun came up and winds from Canada came charging down the Hudson.",
    "I must not fear. Fear is the mind-killer. Fear is the little-death that brings total obliteration. I will face my fear. I will permit it to pass over me and through me. And when it has gone past I will turn the inner eye to see its path. Where the fear has gone there will be nothing. Only I will remain.",
    "Stuff your eyes with wonder, he said, live as if you'd drop dead in ten seconds. See the world. It's more fantastic than any dream made or paid for in factories.",
    "You can tell yourself that you would be willing to lose everything you have in order to get something you want. But it's a catch-22: all of those things you're willing to lose are what make you recognizable. Lose them, and you've lost yourself.",
    "You have brains in your head. You have feet in your shoes. You can steer yourself any direction you choose. You're on your own. And you know what you know. And YOU are the one who'll decide where to go…",
    "I had forgotten that time wasn't fixed like concrete but in fact was fluid as sand, or water. I had forgotten that even misery can end.",
    "If you want to know what a man's like, take a good look at how he treats his inferiors, not his equals.",
    "We are the music-makers, And we are the dreamers of dreams, Wandering by lone sea-breakers, And sitting by desolate streams. World-losers and world-forsakers, Upon whom the pale moon gleams; Yet we are the movers and shakers, Of the world forever, it seems.",
    "The wide world is all about you: you can fence yourselves in, but you cannot for ever fence it out.",
    "There are many Beths in the world, shy and quiet, sitting in corners till needed, and living for others so cheerfully that no one sees the sacrifices till the little cricket on the hearth stops chirping, and the sweet, sunshiny presence vanishes, leaving silence and shadow behind.",
    "But of course we can't take any credit for our talents. It's how we use them that counts.",
    "The rules of the Hunger Games are simple. In punishment for the uprising, each of the twelve districts must provide one girl and one boy, called tributes, to participate. The twenty-four tributes will be imprisoned in a vast outdoor arena that could hold anything from a burning desert to a frozen wasteland. Over a period of several weeks, the competitors must fight to the death. The last tribute standing wins.",
    "It does not do to dwell on dreams and forget to live, remember that. Now, why don't you put that admirable Cloak back on and get off to bed?",
    "Of course it is happening inside your head, Harry, but why on earth should that mean that it is not real?",
]

QUOTES = [
    "The greatest glory in living lies not in never falling, but in rising every time we fall. -Nelson Mandela",
    "Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma - which is living with the results of other people's thinking. -Steve Jobs",
    "If life were predictable it would cease to be life, and be without flavor. -Eleanor Roosevelt",
    "If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough. -Oprah Winfrey",
    "Do not go where the path may lead, go instead where there is no path and leave a trail. -Ralph Waldo Emerson",
    "Tell me and I forget. Teach me and I remember. Involve me and I learn. -Benjamin Franklin",
    "You will face many defeats in life, but never let yourself be defeated. -Maya Angelou",
    "Only a life lived for others is a life worthwhile. -Albert Einstein",
    "Twenty years from now you will be more disappointed by the things that you didn't do than by the ones you did do. So, throw off the bowlines, sail away from safe harbor, catch the trade winds in your sails. Explore, Dream, Discover. -Mark Twain",
    "The mediocre teacher tells. The good teacher explains. The superior teacher demonstrates. The great teacher inspires. -William Arthur Ward",
    "If you can't communicate and talk to other people and get across your ideas, you're giving up your potential. -Warren Buffet",
    "If you can't explain it simply, you don’t understand it well enough. -Albert Einstein",
    "A designer knows he or she has achieved perfection, not when there is nothing left to add, but when there is nothing left to take away. -Nolan Haims",
    "Always do right. This will gratify some people and astonish the rest. -Mark Twain",
    "Never doubt that a small group of thoughtful, committed citizens can change the world. Indeed, it is the only thing that ever has. -Margaret Mead",
    "I'm sorry, but I don't want to be an emperor. That's not my business. I don't want to rule or conquer anyone. I should like to help everyone if possible; Jew, Gentile, black man, white. We all want to help one another. Human beings are like that. We want to live by each other's happiness, not by each other's misery. We don't want to hate and despise one another. In this world there is room for everyone, and the good earth is rich and can provide for everyone. -Charlie Chaplain",
    "Remembering that I'll be dead soon is the most important tool I've ever encountered to help me make the big choices in life. Almost everything - all external expectations, all pride, all fear of embarrassment or failure - these things just fall away in the face of death, leaving only what is truly important. -Steve Jobs",
    "No one wants to die. Even people who want to go to heaven don't want to die to get there. And yet, death is the destination we all share. No one has ever escaped it, and that is how it should be, because death is very likely the single best invention of life. It's life's change agent. It clears out the old to make way for the new. -Steve Jobs",
    "We speak not only to tell other people what we think, but to tell ourselves what we think. Speech is a part of thought. -Oliver Sacks",
    "We may not be able to stop evil in the world, but how we treat one another is entirely up to us. -Barack Obama",
    "The quality of mercy is not straind. It droppeth as the gentle rain from heaven upon the place beneath. It is twice blest: it blesseth him that gives and him that take -William Shakespeare, The Merchant of Venice",
    "I love you the more in that I believe you had liked me for my own sake and for nothing else. -John Keats",
    "Let us sacrifice our today so that our children can have a better tomorrow. -A.P.J. Abdul Kalam",
    "The most difficult thing is the decision to act, the rest is merely tenacity. The fears are paper tigers. You can do anything you decide to do. You can act to change and control your life; and the procedure, the process is its own reward. -Amelia Earhart",
    "Do not mind anything that anyone tells you about anyone else. Judge everyone and everything for yourself. Henry James",
    "Good judgment comes from experience, and a lot of that comes from bad judgment. -Will Rogers",
    "Think in the morning. Act in the noon. Eat in the evening. Sleep in the night. -William Blake",
    "Work like you don't need the money. Love like you've never been hurt. Dance like nobody's watching. -Satchel Paige",
    "If you know the enemy and know yourself, you need not fear the result of a hundred battles. -Sun Tzu, The Art of War",
    "The supreme art of war is to subdue the enemy without fighting. -Sun Tzu, The Art of War",
    "There is only one corner of the universe you can be certain of improving, and that's your own self. -Aldous Huxley",
    "Wise men speak because they have something to say; Fools because they have to say something. -Plato",
    "Always remember that you are absolutely unique. Just like everyone else. -Margaret Mead",
    "The World is my country, all mankind are my brethren, and to do good is my religion. -Thomas Paine",
    "The only true wisdom is in knowing you know nothing. -Socrates",
    "As we express our gratitude, we must never forget that the highest appreciation is not to utter words, but to live by them. -John F. Kennedy",
    "Education is the most powerful weapon which you can use to change the world. -Nelson Mandela",
    "Today you are you! That is truer than true! There is no one alive who is you-er than you! -Dr. Seuss",
    "The only thing necessary for the triumph of evil is for good men to do nothing. -Edmund Burke",
    "Don't judge each day by the harvest you reap but by the seeds that you plant. -Robert Louis Stevenson",
    "It is during our darkest moments that we must focus to see the light. -Aristotle",
    "Where tillage begins, other arts follow. The farmers therefore are the founders of human civilization. -Daniel Webster",
    "Those who cannot remember the past are condemned to repeat it. -George Santayana",
    "The haft of the arrow had been feathered with one of the eagle's own plumes. We often give our enemies the means of our own destruction. -Aesop",
    "The unleashed power of the atom has changed everything save our modes of thinking, and we thus drift toward unparalleled catastrophes. -Albert Einstein",
    "If the brain were so simple we could understand it, we would be so simple we couldn't. -Lyall Watson",
    "Wherever we look, the work of the chemist has raised the level of our civilization and has increased the productive capacity of our nation. -Calvin Coolidge",
    "Better is bread with a happy heart than wealth with vexation. -Amenemope",
    "As soon as men decide that all means are permitted to fight an evil, then their good becomes indistinguishable from the evil that they set out to destroy. -Christopher Dawson",
    "Is it a fact - or have I dreamt it - that, by means of electricity, the world of matter has become a great nerve, vibrating thousands of miles in a breathless point of time? -Nathaniel Hawthorne",
    "The day when two army corps can annihilate each other in one second, all civilized nations, it is to be hoped, will recoil from war and discharge their troops. -Alfred Nobel",
    "A horse, a horse! My kingdom for a horse! -William Shakespeare, Richard III",
    "The press is the best instrument for enlightening the mind of man, and improving him as a rational, moral and social being. -Thomas Jefferson",
    "The speed of communication is wondrous to behold. It is also true that speed can multiply the distribution of information that we know to be untrue. -Edward R. Murrow",
    "There never was a good knife made of bad steel. -Benjamin Franklin",
    "And homeless near a thousand homes I stood, and near a thousand tables pined and wanted food. -William Wordsworth",
    "1. A robot may not injure a human being or, through inaction, allow a human being to come to harm. 2. A robot must obey any orders given to it by human beings, except where such orders would conflict with the First Law. 3. A robot must protect its own existence as long as such protection does not conflict with the First or Second Law. -Isaac Asimov",
    "Pale Death beats equally at the poor man's gate and at the palaces of kings. -Horace",
    "Most of us can, ad we choose, make of the world either a palace or a prison. -John Lubbock",
    "We only live to discover beauty. All else is a form of waiting. -Kahlil Gibran",
    "Every genuine work of art has as much reason for being as the earth and the sun. -Ralph Waldo Emerson",
    "Time crumbles things; everything grows old and is forgotten under the power of time. -Aristotle",
    "The true test of civilization is, not the census, nor the size of cities, nor the crops - no, but the kind of man the country turns out. -Ralph Waldo Emerson",
    "He who knows others is wise; He who know himself is enlightened. -Lao Tzu",
    "Whoever desires to found a state and give it laws, must start with assuming that all men are bad and ever ready to display their vicious nature, whenever they may find occasion for it. -Niccolo Machiavelli",
    "In the country of the blind, the one-eyed man is king. -Erasmus",
    "I have a dream that my four little children will one day live in a nation where they will not be judged by the color of their skin but by the content of their character. I have a dream today. -Martin Luther King Jr.",
]


def get_random_choice(lst: list) -> str:
    """Returns a random string from a list of strings with whitespaces.

    Text is also stripped of trailing and leading whitespaces.
    """

    return random.choice(lst).strip()


def replace_from_text(raw_text: str, symbols: dict) -> str:
    """Replace every symbol/character in the keys of the symbols dictionary
    with the corresponding value for each key.

    For use with get_random_text()."""

    for symbol in symbols:
        raw_text = raw_text.replace(symbol, symbols[symbol])

    return raw_text


def remove_from_text(raw_text: str, symbols: list) -> str:
    """Removes every symbol/character in the symbols list from a given string,
    raw_text.

    For use with get_random_text().
    """

    for symbol in symbols:
        raw_text = raw_text.replace(symbol, "")

    return raw_text


def get_random_text() -> str:
    """Returns a string of randomly generated text."""
    LENGTH = 50

    random_int = random.randint(1, 10000)

    raw_list = brown.words()[random_int : random_int + LENGTH]

    raw_text = " ".join(raw_list)

    raw_text = replace_from_text(
        raw_text, {" ,": ",", " .": ".", " ?": "?", "( ": "(", " )": ")"}
    )
    raw_text = remove_from_text(raw_text, [" ''", " ``", " '"])

    return raw_text


_translate = {
    "Common Phrases": lambda: get_random_choice(COMMON_PHRASES),
    "Facts": lambda: get_random_choice(FACTS),
    "Famous Novel Excerpts": lambda: get_random_choice(NOVEL_EXCERPTS),
    "Famous Quotes": lambda: get_random_choice(QUOTES),
    "Randomly Generated Text": lambda: get_random_text(),
}

if __name__ == "__main__":
    print(get_random_text())
    # print(brown.words()[10:100])