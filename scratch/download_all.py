# -*- coding: utf-8 -*-
import os
import sys
import urllib.request
import urllib.parse
import urllib.error
import json
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scratch.generate_goi import words_data, ILLUSTRATED_WORDS

# English descriptions for the remaining 166 words to generate matching claymation style illustrations
descriptions = {
    "baさbaさ": "a character with wild, dry, messy hair standing up in all directions",
    "あたふた": "a flustered character running around in circles with hands on cheeks in a panic",
    "あっさり": "a plate of simple, fresh salad with light dressing, representing a clean and light meal",
    "あつあつ": "a hot pot dish (nabe) boiling on a portable stove with lots of steam",
    "いささか": "a character looking slightly confused with a question mark above their head",
    "いそいそ": "a character happily dressing up and getting ready to go out on a date",
    "いやいや": "a child refusing food, shaking head and pushing a plate away",
    "いよいよ": "an excited audience waiting in front of a theater stage before showtime",
    "いらいら": "an irritated character tapping their foot with a frustrated expression and anger marks",
    "うかうか": "a character daydreaming with butterfly nearby, ignoring their books",
    "うきうき": "a cheerful character walking with a bounce in their step, feeling happy",
    "うじうじ": "a hesitant character looking down and tapping fingers together, unable to decide",
    "うずうず": "a character sitting at a desk, tapping feet excitedly, eager to run outside and play soccer",
    "うっかり": "a character dropping a set of keys by mistake, looking surprised",
    "うっすら": "a thin layer of morning fog over a calm lake, very subtle",
    "うっとり": "a character looking dreamily at a beautiful starry sky with floating hearts",
    "うとうと": "a character dozing off while reading a book in a cozy armchair",
    "うとうとする": "a character nodding off on a train ride, feeling sleepy",
    "うはうha": "a rich character holding gold coins or bags of money with a huge happy grin",
    "うはうは": "a rich character holding gold coins or bags of money with a huge happy grin",
    "うるうる": "a character with big, teary, emotional eyes on the verge of crying happy tears",
    "うろうろ": "a lost character walking around a crossroad with a map, looking confused",
    "うろちょろ": "a little puppy running around a busy chef's feet in a kitchen, getting in the way",
    "うんざり": "a character plugging their ears with a annoyed face, tired of hearing the same story",
    "うんと": "a huge pile of colorful toys or gifts stacked high",
    "おおよそ": "a rough sketch of a house showing the basic shape",
    "おずおず": "a hesitant character reaching out a hand slowly and shyly",
    "おずおずと": "a shy child offering a flower to someone, looking hesitant",
    "おどおど": "a timid, nervous character stammering and sweating, lacking confidence",
    "おめおめ": "a character bowing with sweat drops, looking shameless or embarrassed",
    "およそ": "a map showing a rough estimate of the distance between two cities",
    "おろおろ": "a flustered character looking around frantically, not knowing what to do",
    "かさかさ": "a dry leaf crumbling in hand, representing dry skin or dry autumn leaves",
    "かちかち": "an ice cube or a frozen solid piece of meat",
    "からから": "a thirsty character in a desert pointing to a dry throat, wanting water",
    "からっと": "crispy golden tempura served on a plate next to a fresh breeze",
    "からり": "a sunny, bright blue sky with a crisp, dry breeze",
    "からりとする": "crispy fried tempura on a plate, looking fresh and non-greasy",
    "かりかり": "crispy crunchy potato chips or bacon strips",
    "かんかん": "an extremely angry character with red face and steam coming out of head",
    "がくがく": "a character with shaking knees after a long mountain hike, looking weak",
    "がくっと": "a line graph showing a sharp plunge downwards, with a disappointed cartoon face looking at it",
    "がさがさ": "a character showing dry, rough hands with a dry texture",
    "がたがた": "a character shivering next to a rattling window during a storm",
    "がたがたする": "a small earthquake causing cups on a shelf to rattle",
    "がたぴし": "an old, creaky wooden door with loose hinges, slightly askew",
    "がちがち": "a shivering character with teeth chattering from extreme cold",
    "がっかり": "a disappointed character slumped in a chair, with head down",
    "がっちり": "a strong character with muscular build showing a solid stance",
    "がびがび": "a piece of bread or cloth that has dried out and become stiff and hard",
    "がやがや": "a busy crowded market scene with speech bubbles representing chatter",
    "がらがら": "an empty train car with no passengers, looking spacious",
    "がらりと": "a sudden shift from a dark cloudy sky to bright sunshine",
    "きちんと": "a perfectly aligned row of books on a shelf, looking neat",
    "きっと": "a character with a firm, determined and serious facial expression",
    "きっぱり": "a character saying 'No' firmly with a hand gesture, looking decisive",
    "きびきび": "a smart worker marching forward briskly with a clipboard, looking organized",
    "きょとん": "a character with wide round eyes and a question mark, looking puzzled",
    "きょろきょろ": "a tourist looking around in all directions in a big, busy city",
    "きらきら": "shiny gold stars sparkling brightly on a night sky background",
    "きりきり": "a character holding their stomach in sharp pain, looking distressed",
    "ぎっしり": "a jar packed tightly with colorful jellybeans, no space left",
    "ぎゅうぎゅう": "clothes stuffed tightly into a suitcase, struggling to close it",
    "ぎらぎら": "a harsh, intense sun shining fiercely down, making a character squint",
    "くすくす": "a character giggling behind their hand in a quiet room, trying to hide a smile",
    "くたくた": "an exhausted character slumped on a couch, completely worn out and tired",
    "くどい": "a plate of food overloaded with heavy sauce and grease, looking overwhelming",
    "くどくど": "a parent lecturing a child with long speech bubbles filled with repetitive text",
    "くねくね": "a winding mountain path or a snake sliding in a zigzag line",
    "くよくよ": "a character crying slightly over a spilled cup of tea, overthinking",
    "ぐいぐい": "a strong character pulling a rope with determination",
    "ぐうぐう": "a character sleeping soundly in bed with cartoon snoring bubbles 'Zzz'",
    "ぐしょぐしょ": "a soggy shoe or cloth dripping with puddle water, looking messy and wet",
    "ぐずぐず": "a slow character dragging their feet, taking a long time to get ready",
    "ぐずぐずする": "a character sitting on bed, hesitating to wake up in the morning",
    "ぐっすり": "a character sleeping deeply in a comfy bed, dreaming peacefully",
    "ぐにゃぐにゃ": "a bent, twisting key or metal rod, showing a flexible, soft shape",
    "ぐにゃり": "a soft, bent plastic spoon or ruler bending easily",
    "ぐらぐら": "a stack of bowls shaking unstably on a table during a tremor",
    "ぐんぐん": "a small plant growing taller rapidly, reaching for the sun",
    "ぐんと": "a plant shoot growing high up, showing a sudden growth spurt",
    "けろっと": "a character who is totally fine and smiling, acting like nothing happened after a small accident",
    "けろり": "a healthy character looking fully recovered from a cold, smiling and energetic",
    "げっそり": "a thin, exhausted character looking tired with hollow cheeks and dark circles under eyes",
    "げらげら": "a character laughing out loud with a wide open mouth and tears of laughter in eyes",
    "げんなり": "a character sighing with a droopy posture, looking completely disappointed or fed up with a stack of paperwork",
    "こそこそ": "two characters whispering secrets to each other sneakily",
    "こちこち": "a character standing stiff like a stone statue due to fright",
    "こっくり": "a character sitting in a chair, nodding off to sleep with eyes closed",
    "こっそり": "a sneaky character tip-toeing in the dark to grab a midnight snack",
    "こってり": "a rich bowl of ramen with thick broth and toppings, looking delicious",
    "こつこつ": "a character carefully stacking blocks one by one to build a tall tower, working diligently",
    "こりこり": "crunchy pork cartilage or squid rings served on a small plate",
    "ころころ": "a few small round marbles rolling down a hill in different directions",
    "こんもり": "a lush, round green hill covered in thick bushes and grass",
    "ごうごう": "a stormy wind howling and blowing trees sideways during a gale",
    "ごくごく": "a thirsty character gulping down a cold glass of milk",
    "ごちゃごちゃ": "a cluttered desk filled with disorganized papers, pens, and wires",
    "ごつごつ": "a rough, rugged character touching coarse, uneven rocks",
    "ごつごつする": "rugged and bumpy stone path with rough textures",
    "ごてごて": "a character wearing way too many necklaces, rings, and colorful hats",
    "ごろごろ": "a character lying down lazily on a cozy rug at home, watching TV with snacks around",
    "さくさく": "a fresh crunchy cookie being bitten in half, showing crumbs",
    "さっさと": "a quick character packing their bag and leaving the room efficiently",
    "さっさとやる": "a character doing house chores quickly and leaving to play",
    "さっぱり": "a character feeling fresh after taking a shower, wearing a clean bathrobe",
    "さっぱりする": "a character feeling fresh after taking a warm bath, wrapping in a towel",
    "さらさら": "silky smooth hair blowing gently in a soft wind",
    "さらっと": "pouring smooth, light lotion onto a clean hand, absorbing instantly",
    "ざあざあ": "heavy rain pouring down in thick sheets, splashing on the ground",
    "ざらざら": "rough sandpaper surface or a sandy beach texture",
    "しくしく": "a character sitting alone crying softly, wiping tears with a handkerchief",
    "しっかり": "a reliable character holding a pole firmly, standing strong",
    "しっとり": "a soft green leaf wet with morning dew, looking fresh",
    "しつこい": "a character trying to shake off a persistent fly buzzing around their head",
    "しとしと": "soft, gentle drizzle falling quietly on a small paper umbrella",
    "しぶしぶ": "a reluctant character doing chores with a sigh and slumped shoulders",
    "しみじみ": "a character sitting quietly, feeling deep emotion or nostalgia with a gentle smile",
    "しゃあしゃあと": "a mischievous character laughing and hiding a broken vase behind their back",
    "しゃきしゃき": "a chef chopping vegetables extremely fast with crisp movements",
    "しゃきっと": "an energetic character stretching arms, feeling fully awake and refreshed after washing face",
    "しゃりしゃり": "a refreshing bowl of shaved ice (kakigori) with syrup",
    "しょんぼり": "a sad character walking in the rain with a droopy posture, looking downcast",
    "しれっと": "a character entering late with a calm, poker face, ignoring the angry teacher",
    "じっくり": "a chef slow-cooking a stew, watching it carefully with patience",
    "じっと": "a character sitting perfectly still, staring intently at a tiny ladybug",
    "じっとり": "sweaty hands or damp clothes on a humid rainy summer day",
    "じめじめ": "a damp, mossy wall with droplets of water in a dark room",
    "じりじり": "a character waiting under a hot baking sun, feeling impatient",
    "じろじろ": "a character staring rudely at someone with wide open eyes",
    "じわじわ": "water spreading slowly across a paper towel, expanding outward",
    "じわーっと": "warm tea diffusing slowly in a cup, creating a gentle gradient",
    "じわーっとする": "a warm compress on a sore shoulder, spreading heat gently",
    "じんじん": "a character holding their cold hands, feeling a tingling or numbing sensation",
    "すかすか": "a box containing only two small items, looking mostly empty",
    "すくすく": "a healthy baby growing taller and smiling, representing healthy growth",
    "すたすた": "a determined character walking past a crowd with quick, firm steps",
    "すっかり": "a glass that is completely empty, all gone",
    "すっきり": "a character stretching arms in a clean, decluttered bedroom, looking refreshed",
    "すっきりする": "a character stretching arms in a clean, decluttered bedroom",
    "すやすや": "a baby sleeping peacefully in a crib with a soft smile",
    "すらすら": "a smart character writing answers on a test paper quickly and smoothly",
    "するする": "a smooth snake gliding effortlessly through tall green grass",
    "するりと": "a wet soap bar slipping easily out of a character's hand",
    "すんなり": "a slender character standing elegantly, looking fit",
    "すーすー": "a character feeling a cool minty breeze in their mouth or neck",
    "すーすーする": "a cool breeze flowing through an open window, cooling a room",
    "ずきずき": "a character holding their cheek due to a throbbing toothache, showing a painful face",
    "ずっしり": "a heavy golden treasure chest sitting on the floor",
    "ずらっと": "a long line of cars parked neatly along a street",
    "ずらり": "a long row of cute toy soldiers lined up perfectly on a shelf",
    "せかせか": "a busy businessman walking very fast with coffee and phone, looking rushed",
    "せっせと": "a hardworking character building a sandcastle or writing notes diligently",
    "そそくさと": "a character leaving a party early, walking away quickly and quietly",
    "そっくり": "two identical twins standing side-by-side, wearing matching clothes",
    "そよそよ": "a gentle breeze swaying green grass and flowers under a calm sky",
    "そろそろ": "a character pointing at a watch, indicating it is time to leave",
    "そわそわ": "an anxious character looking at a clock and tapping their foot, waiting for someone",
    "そわそわする": "a character looking at their phone and pacing back and forth anxiously",
    "ぞっと": "a character shivering in fear with goosebumps, looking terrified by a ghost story",
    "たっぷり": "a bowl overflowing with fresh, delicious fruit salad",
    "だらだら": "a lazy character lying on the floor scrolling on a phone, wasting time",
    "だんだん": "a cute seedling slowly growing taller step by step",
    "ちくちく": "a character touching a cactus or wearing an itchy wool sweater",
    "ちくちくする": "a character touching a spiky hedgehog gently",
    "ちびちび": "a character using a tiny spoon to eat a small dessert, savoring every bit",
    "ちゃくちゃくと": "a house being built brick by brick, progress moving steadily",
    "ちゃっかり": "a clever character smiling playfully while snatching the best seat or a treat, looking self-satisfied",
    "ちゃんとする": "a neat character folding clothes perfectly and placing them in a drawer",
    "ちょくちょく": "a character frequently visiting their favorite bakery, waving to the baker",
    "ちょこちょこ": "a small cute character taking quick, small baby steps",
    "ちょこまか": "a small hyperactive mouse or character scurrying around quickly",
    "ちょっぴり": "a tiny pinch of salt being sprinkled from fingers",
    "ちらちら": "a character peek-a-booing or looking sideways repeatedly, shyly",
    "ちらほら": "a few scattered cherry blossom petals falling gently in the wind",
    "つくづく": "a thoughtful character looking at an old photo, reflecting deeply with a gentle expression",
    "つるつる": "a character sliding smoothly on a clean, polished shiny floor",
    "つるつるする": "a shiny, smooth pearl reflecting light, looking perfect",
    "つれづれ": "a character lying down, looking bored with clock ticking, representing leisure time",
    "つんつん": "a character with crossed arms looking away coldly with a huff",
    "てkぱきやる": "a fast chef chopping vegetables quickly and neatly on a board",
    "てきぱき": "a fast worker sorting documents quickly and efficiently",
    "てきぱきやる": "a fast chef chopping vegetables quickly and neatly on a board",
    "てくてく": "a character walking steadily and happily along a country road",
    "てらてら": "a shiny forehead or a oily bald head reflecting light",
    "てれてれ": "a blushing character scratching their head shyly",
    "とことこ": "a tiny toddler walking cute and steady on a grass field",
    "とぼとぼ": "a sad character walking home with heavy steps and head hanging low",
    "とろとろ": "melted cheese stretching from a hot slice of pizza",
    "どきっと": "a startled character clutching their chest in shock as if their heart skipped a beat",
    "どきどき": "a character with a loudly beating heart, looking nervous and excited before a performance",
    "どっさり": "a huge pile of apples falling out of a basket",
    "どっと": "a sudden crowd of people rushing into a store for a sale",
    "どろどろ": "a character stepping in thick, sticky mud, feet covered in mud",
    "どんどん": "a train speeding fast along a track, moving forward rapidly",
    "どんより": "a gloomy, dark grey cloudy sky over a quiet field",
    "にこにこ": "a cheerful character with a bright, warm smile and happy blushing cheeks",
    "にっこり": "a character smiling warmly with cute blushing cheeks",
    "にやにや": "a mischievous character smiling with a smirk or a playful grin",
    "にやにやする": "a character smirking while planning a funny prank",
    "にやりと": "a character with a clever smirk, having just solved a mystery",
    "ぬきあし": "a character walking on tiptoes quietly, trying not to make a sound",
    "ぬくぬく": "a character wrapped in a warm blanket, drinking hot cocoa, feeling cozy",
    "ぬけぬけと": "a character eating someone else's cake with a cheeky grin",
    "ぬるぬる": "a slippery character trying to hold a wet, slimy bar of soap",
    "ぬるぬるする": "a character sliding on a slimy wet slide with soap bubbles",
    "ねばねば": "a sticky food bowl of natto being lifted with sticky threads stretching",
    "ねばねばする": "a character pulling sticky caramel or natto threads from a plate",
    "のうnうと": "a lazy character lying back on a hammock, eating grapes without a care",
    "のうのうと": "a lazy character lying back on a hammock, eating grapes without a care",
    "のそのそ": "a large slow bear walking lazily through the forest",
    "のびのび": "a happy character lying on green grass under a clear blue sky, arms spread wide in relaxation",
    "のりのり": "a character dancing at a party with hands in the air, full of energy",
    "のろのろ": "a slow snail crawling slowly along a wet leaf",
    "のんびり": "a character relaxing on a beach chair under a palm tree",
    "はあはあ": "a tired character breathing heavily after running, with steam/air puffs from mouth",
    "はきはき": "a confident character speaking clearly with a big smile",
    "はしゃぐ": "a playful child jumping and dancing around excitedly with hands up",
    "はっきり": "a clear mountain view under a bright sun, very distinct and sharp",
    "はっと": "a character suddenly gasping with a lightbulb appearing above their head, realizing something",
    "はらはら": "a nervous parent watching a child walk on a narrow balance beam, feeling anxious",
    "ばさばさ": "a character with wild, dry, messy hair standing up in all directions",
    "ばたばた": "a busy character running around with papers flying, rushing to finish tasks",
    "ばったり": "two characters bumping into each other on a street corner, looking surprised",
    "ばっちり": "a character showing double thumbs up with a perfect score paper",
    "ばらばら": "scattered puzzle pieces lying randomly on a table",
    "ぱさぱさ": "a piece of dry bread crumbling into dust, looking very dry",
    "ぱっちり": "a character with big, bright, wide-open eyes showing curiosity",
    "ぱらぱら": "a character quickly flipping through the pages of a book, pages flying",
    "ひえひえ": "a chilled can of soda covered in condensation droplets",
    "ひそひそ": "two friends whispering quietly in a library, pointing to a book",
    "ひやっと": "a character suddenly startled by a cold ice cube touched to their back",
    "ひやひや": "a nervous character sweating and looking down from a high place, feeling scared",
    "ひやりと": "a character looking down over a steep cliff edge, feeling a sudden chill of fear",
    "ひょっこり": "a cute rabbit popping its head out of a hole in the ground",
    "ひりひり": "a character holding their tongue after eating a hot red chili pepper",
    "ひりひりする": "a character putting aloe vera on a sunburned shoulder",
    "ひんやり": "a character enjoying the cool morning breeze in a forest, feeling refreshed",
    "びriびri": "a character touching a static balloon, showing light electric sparks",
    "びくびく": "a frightened character trembling and looking around warily, afraid of a loud noise",
    "びしょびしょ": "a character completely drenched in water, dripping wet",
    "びっくり": "a shocked character jumping in surprise, with eyes wide open",
    "びっしょり": "a character soaking wet from a sudden rain shower, holding a wet umbrella",
    "びりびり": "a character touching a static balloon, showing light electric sparks",
    "ぴかぴか": "a freshly polished, sparkling clean floor reflecting light",
    "ぴちぴち": "a fresh fish jumping out of a fishing net, full of life",
    "ぴったり": "two puzzle pieces fitting together perfectly",
    "ぴりぴり": "a tense character surrounded by static electricity lines, looking nervous and sensitive",
    "ふうふう": "a character blowing hot soup in a bowl to cool it down",
    "ふっくら": "freshly baked bread rolls, round and plump",
    "ふと": "a character suddenly looking up at a shooting star in the night sky",
    "ふにゃふにゃ": "a character trying to pick up a wet, soft clay toy that is bending easily",
    "ふらふら": "a dizzy character walking unsteadily with spirals in eyes",
    "ふわふわ": "a fluffy sheep or a soft, puffy cloud in the sky",
    "ぶらぶら": "a relaxed character strolling casually in a park on a sunny day",
    "ぶるぶる": "a shivering character shaking from cold weather, teeth chattering",
    "ぷにぷに": "squishy cat paw pads or a soft jelly dessert being poked by a finger",
    "ぷりぷり": "fresh, plump shrimp cooked to perfection, looking bouncy",
    "ぷんすか": "a cute angry character puffing up cheeks and looking away",
    "ぷんぷん": "an angry child character with red cheeks and steam blowing out of ears in a cute cartoon way",
    "へとへと": "a completely drained character lying flat on the floor, out of energy",
    "へなへな": "a character collapsing into a soft heap on the ground due to sudden exhaustion or shock",
    "へらへら": "a silly character laughing foolishly with a goofy, relaxed face",
    "へろへろ": "a runner crossing a finish line, completely limp and wobbly like jelly, out of breath",
    "べたっと": "a tired character lying flat and spread out on a rug",
    "べたべた": "a character with sticky hands covered in glue, looking annoyed",
    "べたべたする": "a child with sticky fingers covered in honey, looking messy",
    "べとべと": "hands covered in sticky honey or maple syrup",
    "ぺこぺこ": "a hungry character with a cartoon growling stomach, dreaming of food",
    "ぺらぺら": "a bilingual character speaking fluently with speech bubbles of different languages",
    "ほかほか": "steaming hot steamed buns (baozi) on a bamboo steamer, soft steam rising",
    "ほくほく": "a hot baked sweet potato cut open, steam rising from the yellow inside",
    "ほっと": "a character sighing with relief, wiping sweat from forehead with a smile",
    "ほとんど": "a glass of juice that is almost empty, only a tiny sip left",
    "ほぼ": "a puzzle that is almost complete, only one piece missing",
    "ぼうぜん": "a stunned character standing still with a blank, empty expression and wide eyes",
    "ぼちぼち": "a character packing their bag slowly, getting ready to leave",
    "ぼろぼろ": "an old, torn teddy bear with patches, looking well-loved but worn out",
    "ぼんやり": "a daydreaming character staring out the window with a blank mind",
    "ぽかぽか": "a happy character sunbathing under warm sunlight, looking cozy and content",
    "ぽかん": "a character with an open mouth and blank eyes, staring in surprise",
    "ぽつぽつ": "a few raindrop splatters falling on a dry pavement",
    "まごまご": "a lost character looking at a complex map at a train station",
    "ますます": "a growing snowman getting bigger as more snow falls",
    "まちまち": "a row of houses in different shapes, sizes, and colors",
    "まったり": "a character slowly sipping warm coffee at a quiet cafe table, looking relaxed",
    "まるごと": "a character biting into a large whole red apple",
    "まるまる": "a chubby, round puppy sleeping happily like a ball",
    "みっしり": "a shelf packed tightly with books, leaving absolutely no gaps",
    "むかつく": "an irritated character clutching their stomach with an angry vein popping on their forehead",
    "むかむか": "a character holding their stomach with a nauseous or angry expression",
    "むしむし": "a character wiping sweat in a hot steam room or humid weather",
    "むずむず": "a character rubbing their nose due to an itchy feeling from pollen",
    "むせ返る": "a character coughing from thick smoke or strong perfume in the air",
    "むっちり": "a cute chubby baby forearm or thigh with soft skin rolls",
    "むっつり": "a grumpy character sitting silently with a stern, expressionless face",
    "むっと": "a character crossing their arms with a pouting and displeased face",
    "むんむん": "a hot, humid crowded train with steam rising, people looking sweaty",
    "めきめき": "a character growing taller and stronger rapidly, with a plant sprout growing next to them",
    "めげる": "a discouraged character sitting with head down, looking sad after a failure",
    "めそめそ": "a crying child wiping tears, whimpering quietly",
    "めちゃくちゃ": "a messy room with toys scattered everywhere and a chaotic bed",
    "めちゃめちゃ": "a broken plate shattered into pieces on the floor",
    "めっきり": "a character putting on a warm coat as the weather suddenly turns cold",
    "もじもじ": "a shy character fidgeting with their hands, blushing",
    "もじもじする": "a shy character twisting their apron and looking away blushingly",
    "もたもた": "a character struggling slowly to button a shirt, looking clumsy",
    "もたもたする": "a clumsy character struggling to tie shoelaces slowly",
    "もちもち": "soft, stretchy mochi cakes being pulled apart, looking chewy",
    "もやもや": "a character with a foggy cloud around their head, feeling confused and hazy",
    "もんもん": "a worried character sitting with chin in hand, deep in troubled thoughts with swirl lines around",
    "やきもき": "a worried character pacing back and forth, anxious about late news",
    "やんわり": "a hand gently waving stop, refusing something politely",
    "ゆうゆうと": "a character relaxing on a floatie in a calm pool, looking confident",
    "ゆったりする": "a character relaxing in a hot spring (onsen), looking peaceful",
    "ゆらゆら": "a single candle flame flickering gently in a soft breeze",
    "よちよち": "a cute baby penguin walking with wobbly steps on snow",
    "よろよろ": "a dizzy, unsteady character walking with wobbly legs, almost falling",
    "るんるん": "a happy character skipping down a street with music notes floating around",
    "わいわい": "a group of happy friends cheering and laughing together at a table",
    "わくわく": "an excited character with shining eyes, looking forward to a trip",
    "わずか": "a piggy bank containing only a single coin, representing very little",
    "カラリとする": "crisp, dry clothes hanging on a line under a bright sun",
    "ゾクゾク": "a shivering character wrapped in a blanket, feeling a cold chill or goosebumps",
    "堂々と": "a proud character standing tall on a podium with a chest puffed out",
}

def main():
    print("BẮT ĐẦU TẢI ẢNH MINH HỌA TỰ ĐỘNG TỪ POLLINATIONS.AI...")
    dest_dir = "/Users/tuyennq1001/htdocs/jlpt-n1/goi/images/onomatopoeia"
    os.makedirs(dest_dir, exist_ok=True)
    
    # Danh sách các từ cần tải ảnh (gồm các từ chưa có ánh xạ HOẶC tệp ảnh trên đĩa bị thiếu/rỗng)
    words_to_download = []
    for item in words_data:
        word = item[0]
        dest_filename = ILLUSTRATED_WORDS[word] if word in ILLUSTRATED_WORDS else f"{word}.png"
        dest_path = os.path.join(dest_dir, dest_filename)
        if word not in ILLUSTRATED_WORDS or not os.path.exists(dest_path) or os.path.getsize(dest_path) == 0:
            words_to_download.append(word)
            
    print(f"Tổng số từ cần tải ảnh: {len(words_to_download)}")
    
    downloaded_count = 0
    new_illustrated_words = {}
    
    for word in words_to_download:
        if word not in descriptions:
            print(f"Bỏ qua '{word}' vì không tìm thấy mô tả prompt.")
            continue
            
        desc = descriptions[word]
        # Xây dựng prompt đất sét 3D đầy đủ
        prompt = f"Cute and simple 3D claymation style illustration of {desc}, cozy pastel colors, isolated on a clean soft background"
        
        # URL encode prompt
        encoded_prompt = urllib.parse.quote(prompt)
        
        dest_filename = ILLUSTRATED_WORDS[word] if word in ILLUSTRATED_WORDS else f"{word}.png"
        dest_path = os.path.join(dest_dir, dest_filename)
        
        # Kiểm tra xem tệp ảnh đã tồn tại và hợp lệ (lớn hơn 0 bytes) chưa để tránh tải trùng lặp
        if os.path.exists(dest_path) and os.path.getsize(dest_path) > 0:
            print(f"  -> Tệp ảnh đã tồn tại: {dest_filename} (Bỏ qua tải xuống, tự động thêm ánh xạ)")
            new_illustrated_words[word] = dest_filename
            update_generate_goi_script({word: dest_filename})
            os.system("python3 scratch/generate_goi.py")
            continue
            
        success = False
        retries = 3
        
        while retries > 0 and not success:
            import random
            seed = random.randint(1, 100000)
            url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=512&height=512&nologo=true&seed={seed}"
            print(f"Đang tải ảnh cho '{word}'...")
            try:
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req, timeout=15) as response:
                    if response.status == 200:
                        data = response.read()
                        
                        # Kiểm tra xem dữ liệu có phải là JSON lỗi không (chứa x402Version hoặc Queue full)
                        if b"Queue full" in data or b"x402Version" in data:
                            print(f"  -> Bị giới hạn hàng chờ (Queue full). Đang nghỉ 25 giây trước khi thử lại (còn {retries-1} lượt thử)...")
                            time.sleep(25)
                            retries -= 1
                            continue
                            
                        if len(data) > 0:
                            with open(dest_path, 'wb') as f:
                                f.write(data)
                            print(f"  -> Đã lưu: {dest_filename}")
                            new_illustrated_words[word] = dest_filename
                            downloaded_count += 1
                            update_generate_goi_script({word: dest_filename})
                            os.system("python3 scratch/generate_goi.py")
                            success = True
                        else:
                            print(f"  -> Lỗi: Tải về tệp trống (0 bytes). Thử lại sau 10 giây (còn {retries-1} lượt thử)...")
                            time.sleep(10)
                            retries -= 1
                    else:
                        print(f"  -> Lỗi kết nối: {response.status}. Thử lại sau 10 giây (còn {retries-1} lượt thử)...")
                        time.sleep(10)
                        retries -= 1
            except urllib.error.HTTPError as e:
                if e.code == 402:
                    print(f"  -> Bị chặn 402 (Queue full/Rate limit). Đang nghỉ 25 giây trước khi thử lại (còn {retries-1} lượt thử)...")
                    time.sleep(25)
                    retries -= 1
                else:
                    print(f"  -> Lỗi HTTP {e.code}: {e.reason}. Thử lại sau 10 giây (còn {retries-1} lượt thử)...")
                    time.sleep(10)
                    retries -= 1
            except Exception as e:
                print(f"  -> Lỗi tải ảnh: {e}. Thử lại sau 10 giây (còn {retries-1} lượt thử)...")
                time.sleep(10)
                retries -= 1
                
        # Thêm khoảng nghỉ 3 giây giữa các lượt tải thành công/thất bại hoàn toàn
        time.sleep(3)
            
    print(f"\nĐã hoàn thành! Tải thành công {downloaded_count} ảnh minh họa mới.")

def update_generate_goi_script(new_illustrated):
    script_path = "/Users/tuyennq1001/htdocs/jlpt-n1/scratch/generate_goi.py"
    with open(script_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Tìm đoạn ILLUSTRATED_WORDS = { ... } và chèn các mục mới vào
    lines = content.splitlines()
    dict_start_idx = -1
    dict_end_idx = -1
    
    for idx, line in enumerate(lines):
        if "ILLUSTRATED_WORDS = {" in line:
            dict_start_idx = idx
            break
            
    if dict_start_idx != -1:
        # Tìm dấu đóng ngoặc }
        for idx in range(dict_start_idx, len(lines)):
            if "}" in lines[idx]:
                dict_end_idx = idx
                break
                
    if dict_start_idx != -1 and dict_end_idx != -1:
        # Lấy các cặp key-value hiện tại
        existing_items = []
        for idx in range(dict_start_idx + 1, dict_end_idx):
            line = lines[idx].strip()
            if line:
                existing_items.append(line)
                
        # Thêm các cặp mới
        for word, filename in new_illustrated.items():
            # Kiểm tra xem từ này đã tồn tại trong existing_items chưa
            already_exists = False
            for item in existing_items:
                if f'"{word}":' in item or f"'{word}':" in item:
                    already_exists = True
                    break
            if not already_exists:
                # Format: "word": "filename",
                existing_items.append(f'    "{word}": "{filename}",')
            
        # Nối lại nội dung dict mới
        dict_content = "ILLUSTRATED_WORDS = {\n" + "\n".join(existing_items) + "\n}"
        
        # Thay thế đoạn dict cũ bằng dict mới
        new_lines = lines[:dict_start_idx] + [dict_content] + lines[dict_end_idx + 1:]
        
        with open(script_path, "w", encoding="utf-8") as f:
            f.write("\n".join(new_lines))

if __name__ == "__main__":
    main()
