#!/usr/bin/env python3
"""Part A: generate 50 kids/tweens exercises. Part B: update sports_suggested."""
import json, os

SRC = os.path.join(os.path.dirname(__file__), '..', 'data', 'exercises.json')

SOURCE_NOTE = (
    "MET values estimated from Compendium of Physical Activities (Ainsworth et al. 2011) "
    "and ACSM/NSCA Youth Exercise Guidelines; calories = MET × weight_kg / 60 per minute; "
    "weight assumed 35 kg (Kids 6-9), 45 kg (Tweens 10-12), 40 kg (mixed)."
)

def build_ex(d):
    wt = d.get('wt', 40)
    met = d.get('met', 3.5)
    dur = d.get('dur', 1.0)
    cal_pm = round(met * wt / 60, 1)
    cal_est = round(cal_pm * dur, 1)
    role = d.get('pres_role', 'strength')
    pres = d.get('pres', {'sets': 2, 'reps': 10, 'rest_seconds': 30, 'tempo': 'controlled'})
    return {
        "id": d['id'],
        "slug": d['slug'],
        "name": d['name'],
        "description": d['desc'],
        "level": d.get('level', 'Beginner'),
        "primary_focus": d.get('focus', 'Coordination'),
        "body_area": None,
        "equipment": ["bodyweight"],
        "primary_muscles": d.get('pm', []),
        "secondary_muscles": d.get('sm', []),
        "stabilizer_muscles": d.get('st', []),
        "muscles_subregions": d.get('sub', []),
        "movement_pattern": d['mp'],
        "family": d.get('family', d['slug']),
        "difficulty_rank": d.get('dr', 1),
        "workout_roles": d.get('roles', ['warmup', 'main']),
        "sports": d.get('sports', []),
        "goals": d.get('goals', ['improve_coordination', 'home_workout', 'improve_balance']),
        "settings": d.get('settings', ['home', 'outdoor', 'gym', 'school']),
        "tags": d.get('tags', ['low_impact', 'beginner_friendly', 'kids_friendly']),
        "contraindications": d.get('contra', []),
        "narration_script": None,
        "popularity": None,
        "variant_of": None,
        "instructions": {
            "form": d.get('form', []),
            "proTips": d.get('tips', []),
            "commonMistakes": d.get('mistakes', [])
        },
        "classification": {
            "family": d.get('family', d['slug']),
            "isPerSide": d.get('per_side', False),
            "unilateral": d.get('uni', False),
            "energySystem": d.get('energy_sys', 'glycolytic'),
            "kineticChain": d.get('chain', 'closed'),
            "planeOfMotion": d.get('plane', ['sagittal']),
            "bodyweightOnly": True,
            "difficultyRank": d.get('dr', 1),
            "movementPattern": d['mp'],
            "contractionTypes": d.get('ct', ['concentric', 'eccentric']),
            "compoundOrIsolation": d.get('ci', 'compound')
        },
        "demands": {
            "cns": d.get('cns', 'low'),
            "noise": d.get('noise', 'quiet'),
            "space": d.get('space', 'medium'),
            "stability": d.get('stab', 'medium')
        },
        "prescription": {
            "isHold": d.get('is_hold', False),
            "default": {role: pres},
            "defaultHoldSeconds": d.get('hold_secs', None)
        },
        "energy": {
            "metValue": met,
            "sourceNote": SOURCE_NOTE,
            "durationMinutes": dur,
            "caloriesEstimate": cal_est,
            "caloriesPerMinute": cal_pm,
            "assumedUserWeightKg": wt,
            "proteinPostWorkoutG": None
        },
        "timing": {
            "repSecondsEstimate": d.get('rep_secs', None),
            "videoPortraitSeconds": None,
            "videoLandscapeSeconds": None
        },
        "media": {
            "image": {"path": None, "available": False},
            "videoPortrait": {"path": None, "available": False},
            "videoLandscape": {"path": None, "available": False}
        },
        "cv": None,
        "alternatives": [],
        "_raw": None,
        "taxonomy": {
            "age_bands_suggested": d['bands'],
            "age_bands_confirmed": None,
            "sports_suggested": d.get('tax_sports', []),
            "sports_confirmed": None,
            "position": [],
            "position_confirmed": None,
            "movement_type": d.get('mt', 'cardio'),
            "difficulty": d.get('diff', 'beginner'),
            "structure": d.get('struct', 'main'),
            "safety_flags": d.get('flags', [])
        },
        "review_status": "pending"
    }

# ── PART A: NEW EXERCISES ──────────────────────────────────────────────────────

KIDS_ONLY  = ["Kids"]
BOTH       = ["Kids", "Tweens"]
TWEENS_ONLY = ["Tweens"]

DEFS = [

    # ── ANIMAL WALKS – Kids only ──────────────────────────────────────────────
    dict(
        id="kids-ex-0001", slug="duck-walk", name="Duck Walk",
        desc="A fun animal-themed lower body exercise where children squat low and waddle forward like a duck, building quad strength, hip mobility, and coordination in a playful way.",
        focus="Coordination", pm=["quads"], sm=["glutes","core"], st=["ankles"],
        sub=["hip flexors","knee extensors"], mp="locomotion", family="animal-walks",
        dr=1, roles=["warmup","main"], bands=KIDS_ONLY, mt="cardio", diff="beginner", struct="main",
        goals=["improve_coordination","improve_mobility","improve_balance","home_workout"],
        tags=["low_impact","beginner_friendly","kids_friendly","games_based","fun"],
        form=[
            "Stand with feet hip-width apart and squat down so your thighs are parallel to the floor.",
            "Keep your hands on your knees or out in front for balance.",
            "Waddle forward one step at a time, keeping the squat low.",
            "Try to stay as low as possible — quack like a duck if you want!",
            "Walk 5–10 metres then stand up and rest."
        ],
        tips=["Keep your chest up and look forward, not at the ground.",
              "Try to keep both feet flat on the floor as you step."],
        mistakes=["Letting the knees collapse inward — keep them tracking over toes.",
                  "Rising out of the squat between steps — stay low the whole way."],
        wt=35, met=3.8, dur=0.8,
        energy_sys="glycolytic", chain="closed", plane=["sagittal"], ct=["concentric","eccentric"], ci="compound",
        cns="low", noise="quiet", space="medium", stab="medium",
        pres_role="cardio", pres={"sets": 2, "duration_seconds": 20, "rest_seconds": 30},
    ),

    dict(
        id="kids-ex-0002", slug="inchworm-walk", name="Inchworm Walk",
        desc="A full-body mobility and strength movement where children walk their hands out to a plank then walk their feet in, mimicking an inchworm — great for hamstring flexibility and upper body activation.",
        focus="Flexibility", pm=["hamstrings"], sm=["core","shoulders","chest"], st=["wrists"],
        sub=["posterior chain","hip flexors"], mp="mobility", family="inchworm-variations",
        dr=2, roles=["warmup","main"], bands=KIDS_ONLY, mt="mobility", diff="beginner", struct="main",
        goals=["improve_flexibility","improve_mobility","improve_coordination","home_workout"],
        tags=["low_impact","beginner_friendly","kids_friendly","full_body"],
        form=[
            "Stand tall with feet hip-width apart.",
            "Bend forward and place your hands on the floor in front of your feet.",
            "Walk your hands forward until you are in a high plank position.",
            "Hold for a second — your body should be a straight line.",
            "Walk your feet towards your hands (keeping legs as straight as comfortable), then stand up.",
            "That is one rep — repeat across the room!"
        ],
        tips=["Keep your core tight when you're in the plank — don't let your hips sag.",
              "If your hamstrings are tight, bend your knees a little when walking your feet in."],
        mistakes=["Letting the lower back arch in the plank — brace your tummy.",
                  "Rushing through — slow, controlled movement gives the best stretch."],
        wt=35, met=3.5, dur=1.0,
        energy_sys="phosphagen", chain="closed", plane=["sagittal"], ct=["concentric","eccentric","isometric"], ci="compound",
        cns="low", noise="quiet", space="medium", stab="medium",
        pres_role="mobility", pres={"sets": 2, "reps": 6, "rest_seconds": 30, "tempo": "slow"},
    ),

    dict(
        id="kids-ex-0003", slug="kangaroo-hop", name="Kangaroo Hop",
        desc="A playful two-footed jumping movement where children crouch then explode upward and forward like a kangaroo, building leg power, coordination, and explosive athleticism.",
        focus="Power", pm=["quads","glutes"], sm=["calves","core"], st=["ankles"],
        sub=["knee extensors","hip extensors"], mp="plyometric", family="animal-jumps",
        dr=1, roles=["warmup","main"], bands=KIDS_ONLY, mt="cardio", diff="beginner", struct="main",
        goals=["improve_coordination","improve_power","home_workout","improve_balance"],
        tags=["low_impact","beginner_friendly","kids_friendly","games_based","plyometric","fun"],
        form=[
            "Stand with feet hip-width apart and arms by your sides.",
            "Swing your arms back and bend your knees into a small squat.",
            "Swing your arms forward and jump with both feet, landing softly.",
            "Land with bent knees to absorb the impact — be a bouncy kangaroo!",
            "Immediately crouch and hop again, travelling forward."
        ],
        tips=["Use your arms to help you jump further — swing them forward as you take off.",
              "Land toe-heel to absorb the force gently on your joints."],
        mistakes=["Landing stiff-legged — always bend your knees when you land.",
                  "Looking down — keep your eyes forward to maintain balance."],
        wt=35, met=5.0, dur=0.7,
        energy_sys="phosphagen", chain="closed", plane=["sagittal"], ct=["concentric","eccentric"], ci="compound",
        cns="medium", noise="moderate", space="medium", stab="medium",
        pres_role="cardio", pres={"sets": 2, "duration_seconds": 20, "rest_seconds": 30},
        rep_secs=1.5,
    ),

    dict(
        id="kids-ex-0004", slug="bunny-hop", name="Bunny Hop",
        desc="A side-to-side two-footed lateral jump where children bounce like a bunny, developing lateral coordination, ankle strength, and rhythmic movement timing.",
        focus="Coordination", pm=["calves","quads"], sm=["glutes","core"], st=["ankles"],
        sub=["peroneus longus","tibialis anterior"], mp="plyometric", family="lateral-jumps",
        dr=1, roles=["warmup","main"], bands=KIDS_ONLY, mt="cardio", diff="beginner", struct="main",
        goals=["improve_coordination","improve_balance","home_workout"],
        tags=["low_impact","beginner_friendly","kids_friendly","games_based","plyometric","fun"],
        form=[
            "Stand with feet together and arms relaxed at your sides.",
            "Bend your knees slightly and jump to the right with both feet together.",
            "Land softly, bend your knees, then immediately jump to the left.",
            "Keep jumping side to side in a steady rhythm — like a bunny zigzagging!",
            "Try to keep your feet together the whole time."
        ],
        tips=["Keep the jumps small and quick — speed and rhythm matter more than height.",
              "Use your arms for balance, keeping them slightly bent."],
        mistakes=["Jumping too high — small, controlled hops are better.",
                  "Letting feet land apart — keep them together like a bunny's paws."],
        wt=35, met=4.5, dur=0.7,
        energy_sys="phosphagen", chain="closed", plane=["frontal"], ct=["concentric","eccentric"], ci="compound",
        cns="low", noise="moderate", space="low", stab="medium",
        pres_role="cardio", pres={"sets": 2, "duration_seconds": 20, "rest_seconds": 30},
        rep_secs=0.7,
    ),

    dict(
        id="kids-ex-0005", slug="gorilla-walk", name="Gorilla Walk",
        desc="A weight-bearing upper-body and hip mobility drill where children bend forward, let their knuckles graze the floor, and lumber along like a gorilla — great for shoulder girdle activation and proprioception.",
        focus="Coordination", pm=["shoulders","back"], sm=["core","glutes","hamstrings"], st=["wrists"],
        sub=["rhomboids","hip extensors"], mp="locomotion", family="animal-walks",
        dr=1, roles=["warmup","main"], bands=KIDS_ONLY, mt="strength", diff="beginner", struct="main",
        goals=["improve_coordination","build_upper_body","home_workout"],
        tags=["low_impact","beginner_friendly","kids_friendly","games_based","fun"],
        form=[
            "Stand with feet wider than shoulder-width and bend forward at the hips.",
            "Let your arms hang down — fingertips or knuckles touching the floor lightly.",
            "Lumber forward, moving the opposite arm and leg together (right arm, left foot then left arm, right foot).",
            "Stay bent forward and take big, slow steps — roar like a gorilla if you like!",
            "Walk 5–8 metres, then stand up and rest."
        ],
        tips=["Keep a slight bend in the knees to protect your lower back.",
              "Let the movement feel heavy and slow — gorillas don't rush."],
        mistakes=["Rounding the lower back excessively — hinge from the hips, keep a neutral spine.",
                  "Fully bearing weight on wrists — only graze the floor lightly."],
        wt=35, met=3.5, dur=0.8,
        energy_sys="glycolytic", chain="closed", plane=["sagittal","transverse"], ct=["concentric","eccentric"], ci="compound",
        cns="low", noise="quiet", space="medium", stab="medium",
        pres_role="cardio", pres={"sets": 2, "duration_seconds": 20, "rest_seconds": 30},
    ),

    dict(
        id="kids-ex-0006", slug="penguin-waddle", name="Penguin Waddle",
        desc="A playful balance and hip mobility exercise where children stand on their heels, keep toes up, and waddle side to side like a penguin — improving ankle dorsiflexion and lateral hip stability.",
        focus="Balance", pm=["glutes","hip_abductors"], sm=["core","calves"], st=["ankles"],
        sub=["gluteus medius","tibialis anterior"], mp="locomotion", family="animal-walks",
        dr=1, roles=["warmup"], bands=KIDS_ONLY, mt="mobility", diff="beginner", struct="main",
        goals=["improve_balance","improve_coordination","home_workout"],
        tags=["low_impact","beginner_friendly","kids_friendly","games_based","fun"],
        form=[
            "Stand with feet hip-width apart, toes pointing slightly outward.",
            "Lift your toes off the floor so you're balancing on your heels.",
            "Keep your arms tight to your sides like penguin flippers.",
            "Waddle forward by swaying side to side, taking tiny heel steps.",
            "Waddle 5 metres then turn around — squawk like a penguin!"
        ],
        tips=["Keep your chest up and look straight ahead.",
              "Take small steps — waddling is all about the side-to-side sway."],
        mistakes=["Letting the toes drop — keep them lifted throughout.",
                  "Leaning too far forward — stand tall like a proud penguin."],
        wt=35, met=2.8, dur=0.8,
        energy_sys="phosphagen", chain="closed", plane=["frontal"], ct=["concentric","isometric"], ci="compound",
        cns="low", noise="quiet", space="medium", stab="high",
        pres_role="cardio", pres={"sets": 2, "duration_seconds": 20, "rest_seconds": 20},
    ),

    dict(
        id="kids-ex-0007", slug="seal-walk", name="Seal Walk",
        desc="An upper-body and core strength exercise where children lie face-down and drag their body forward using only their arms, like a seal scooting on land — building shoulder, chest, and core endurance.",
        focus="Strength", pm=["shoulders","chest"], sm=["core","triceps"], st=["wrists"],
        sub=["anterior deltoid","pectoralis minor","serratus anterior"], mp="locomotion", family="animal-walks",
        dr=2, roles=["main"], bands=KIDS_ONLY, mt="strength", diff="beginner", struct="main",
        goals=["build_upper_body","improve_coordination","home_workout"],
        tags=["low_impact","beginner_friendly","kids_friendly","games_based","fun","upper_body"],
        form=[
            "Lie face-down on a smooth floor with your hands flat under your shoulders.",
            "Keep your legs fully straight and together — these are your tail flippers!",
            "Push down through your hands and drag yourself forward using only your arms.",
            "Let your legs and lower body trail passively along the floor.",
            "Travel 5–8 metres, then rest."
        ],
        tips=["Press through the whole palm, not just the fingertips.",
              "Keep your core braced to stop your lower back sagging."],
        mistakes=["Using the legs to push — seals don't kick, they glide.",
                  "Letting the head drop — keep your gaze slightly forward."],
        wt=35, met=3.8, dur=0.8,
        energy_sys="glycolytic", chain="closed", plane=["sagittal"], ct=["concentric"], ci="compound",
        cns="low", noise="quiet", space="medium", stab="low",
        pres_role="strength", pres={"sets": 2, "reps": 8, "rest_seconds": 40, "tempo": "controlled"},
    ),

    dict(
        id="kids-ex-0008", slug="log-roll", name="Log Roll",
        desc="A vestibular and body-awareness drill where children lie straight and roll sideways across the floor like a rolling log — improving spatial orientation, coordination, and core activation.",
        focus="Coordination", pm=["core"], sm=["back","shoulders"], st=[],
        sub=["obliques","vestibular system"], mp="mobility", family="ground-movement",
        dr=1, roles=["warmup","main"], bands=KIDS_ONLY, mt="mobility", diff="beginner", struct="main",
        goals=["improve_coordination","improve_balance","home_workout"],
        tags=["low_impact","beginner_friendly","kids_friendly","games_based","fun","vestibular"],
        form=[
            "Lie flat on your back with arms stretched above your head, legs straight.",
            "Keep your body as straight as a log — arms and legs together.",
            "Roll sideways in one direction, keeping your whole body stiff and straight.",
            "Roll 2–3 times in one direction, then stop, and roll back the other way.",
            "Try not to bend at the hips or use your arms to push."
        ],
        tips=["Imagine you are a pencil rolling across the floor — stay long and straight.",
              "Keep your eyes open and fixed on one point to avoid dizziness."],
        mistakes=["Bending the knees or hips — keep the whole body rigid.",
                  "Using hands to steer — the movement should come from the core."],
        wt=35, met=2.5, dur=0.7,
        energy_sys="phosphagen", chain="open", plane=["transverse"], ct=["isometric"], ci="compound",
        cns="low", noise="quiet", space="medium", stab="low",
        pres_role="mobility", pres={"sets": 2, "reps": 4, "rest_seconds": 20, "tempo": "controlled"},
    ),

    dict(
        id="kids-ex-0009", slug="caterpillar-crawl", name="Caterpillar Crawl",
        desc="A worm-like ground mobility sequence where children in a plank inch their feet towards their hands, then walk their hands back out — combining hamstring flexibility with shoulder and core strength in a playful pattern.",
        focus="Flexibility", pm=["hamstrings","core"], sm=["shoulders","calves"], st=["wrists"],
        sub=["posterior chain","hip flexors"], mp="mobility", family="ground-movement",
        dr=2, roles=["warmup","main"], bands=KIDS_ONLY, mt="mobility", diff="beginner", struct="main",
        goals=["improve_flexibility","improve_coordination","home_workout","improve_mobility"],
        tags=["low_impact","beginner_friendly","kids_friendly","games_based","full_body","fun"],
        form=[
            "Start in a high plank with hands under your shoulders, body straight.",
            "Keep your hands still and walk your feet forward in tiny steps until you feel a stretch in your legs.",
            "Hold for a second — you should look like a caterpillar hump!",
            "Then keep your feet still and walk your hands back out to plank.",
            "That is one cycle. Creep forward and repeat."
        ],
        tips=["Move slowly and feel the stretch each time your feet come in.",
              "Keep your legs as straight as comfortable — slight bend is fine."],
        mistakes=["Rushing — slow movement gives the best flexibility benefit.",
                  "Letting the lower back arch when walking hands out."],
        wt=35, met=3.5, dur=1.0,
        energy_sys="phosphagen", chain="closed", plane=["sagittal"], ct=["concentric","eccentric","isometric"], ci="compound",
        cns="low", noise="quiet", space="medium", stab="medium",
        pres_role="mobility", pres={"sets": 2, "reps": 6, "rest_seconds": 30, "tempo": "slow"},
    ),

    dict(
        id="kids-ex-0010", slug="crocodile-crawl", name="Crocodile Crawl",
        desc="A low-to-the-ground contralateral crawling pattern where children keep their belly close to the floor and pull themselves forward with alternating arm-and-leg action, like a crocodile — building cross-body coordination and core strength.",
        focus="Coordination", pm=["core","shoulders"], sm=["glutes","back"], st=["wrists","ankles"],
        sub=["obliques","serratus anterior","hip extensors"], mp="locomotion", family="animal-walks",
        dr=2, roles=["warmup","main"], bands=KIDS_ONLY, mt="strength", diff="beginner", struct="main",
        goals=["improve_coordination","build_core","home_workout"],
        tags=["low_impact","beginner_friendly","kids_friendly","games_based","fun","core"],
        form=[
            "Lie face-down and bend your elbows so your forearms are on the floor.",
            "Pull your right elbow back while pushing off with your left foot — crawl forward!",
            "Then pull your left elbow back while pushing off with your right foot.",
            "Keep your belly low and your body flat — like a real crocodile sneaking up on prey.",
            "Crawl 5–8 metres, then rest."
        ],
        tips=["Move the opposite arm and leg at the same time — this is the cross-body pattern.",
              "Keep your head low and neutral, not craned up."],
        mistakes=["Pushing up off the floor — stay belly-close to the ground.",
                  "Moving the same arm and leg together — this breaks the coordination pattern."],
        wt=35, met=4.0, dur=0.8,
        energy_sys="glycolytic", chain="closed", plane=["sagittal","transverse"], ct=["concentric"], ci="compound",
        cns="medium", noise="quiet", space="medium", stab="low",
        pres_role="strength", pres={"sets": 2, "reps": 8, "rest_seconds": 40, "tempo": "controlled"},
    ),

    dict(
        id="kids-ex-0011", slug="elephant-stomp-walk", name="Elephant Stomp Walk",
        desc="A heavy-footed locomotion game where children hinge forward, let their arms hang like a trunk, and stomp exaggeratedly forward — developing hip hinge mechanics, hamstring flexibility, and playful body awareness.",
        focus="Flexibility", pm=["hamstrings","back"], sm=["glutes","calves"], st=["core"],
        sub=["erector spinae","hip extensors"], mp="locomotion", family="animal-walks",
        dr=1, roles=["warmup","main"], bands=KIDS_ONLY, mt="mobility", diff="beginner", struct="main",
        goals=["improve_flexibility","improve_coordination","home_workout","improve_mobility"],
        tags=["low_impact","beginner_friendly","kids_friendly","games_based","fun"],
        form=[
            "Stand with feet hip-width apart, then hinge forward at the hips with a flat back.",
            "Let your arms hang down and clasp your hands together to make an elephant trunk.",
            "Stomp slowly forward, swinging your trunk from side to side with each step.",
            "Keep your back flat and feel the stretch in the back of your legs.",
            "Trumpet loudly if you want — then walk back and repeat!"
        ],
        tips=["Push your hips back as you hinge — it should feel like a hamstring stretch.",
              "Keep your gaze slightly forward so your neck stays neutral."],
        mistakes=["Rounding the lower back — aim for a flat spine hinge.",
                  "Bending the knees too much — aim to feel a gentle leg stretch."],
        wt=35, met=3.2, dur=0.8,
        energy_sys="phosphagen", chain="closed", plane=["sagittal"], ct=["isometric","concentric"], ci="compound",
        cns="low", noise="quiet", space="medium", stab="medium",
        pres_role="mobility", pres={"sets": 2, "duration_seconds": 20, "rest_seconds": 20, "tempo": "slow"},
    ),

    dict(
        id="kids-ex-0012", slug="flamingo-stand", name="Flamingo Stand",
        desc="A single-leg static balance challenge where children stand on one foot with the other leg raised — like a flamingo — building proprioception, ankle stability, and concentration.",
        focus="Balance", pm=["calves","glutes"], sm=["core","hip_abductors"], st=["ankles"],
        sub=["gluteus medius","tibialis anterior","peroneus longus"], mp="hold", family="balance-challenges",
        dr=1, roles=["warmup","main"], bands=KIDS_ONLY, mt="mobility", diff="beginner", struct="main",
        goals=["improve_balance","improve_coordination","home_workout"],
        tags=["low_impact","beginner_friendly","kids_friendly","balance","fun"],
        form=[
            "Stand tall with feet together and arms relaxed at your sides.",
            "Slowly lift your right foot off the floor and bend the knee, bringing it up like a flamingo leg.",
            "Hold your balance on your left foot — spread your toes for grip.",
            "Try to hold for 10–20 seconds, then switch legs.",
            "For an extra challenge, close your eyes or reach one arm out to the side."
        ],
        tips=["Fix your gaze on a spot on the wall to help with balance.",
              "Spread your toes wide on the standing foot for a bigger base of support."],
        mistakes=["Gripping with the toes — try to keep them relaxed but spread.",
                  "Leaning heavily to one side — keep hips level like a flamingo."],
        wt=35, met=2.0, dur=0.5,
        energy_sys="phosphagen", chain="closed", plane=["frontal"], ct=["isometric"], ci="isolation",
        cns="low", noise="quiet", space="low", stab="high",
        is_hold=True, hold_secs=15,
        pres_role="mobility", pres={"sets": 3, "duration_seconds": 15, "rest_seconds": 15, "tempo": "static"},
        rep_secs=15,
    ),

    dict(
        id="kids-ex-0013", slug="star-jump", name="Star Jump",
        desc="A full-body explosive jumping exercise where children leap into the air spreading their arms and legs wide like a star before landing — combining cardio, coordination, and total-body movement.",
        focus="Cardio", pm=["quads","glutes"], sm=["calves","shoulders","core"], st=["ankles"],
        sub=["hip abductors","deltoids"], mp="plyometric", family="jumping-games",
        dr=1, roles=["warmup","main"], bands=KIDS_ONLY, mt="cardio", diff="beginner", struct="main",
        goals=["improve_coordination","improve_cardio","home_workout","improve_power"],
        tags=["low_impact","beginner_friendly","kids_friendly","cardio","fun","plyometric"],
        form=[
            "Stand with feet together and arms by your sides.",
            "Bend your knees slightly, then jump up as high as you can.",
            "In the air, spread your legs wide and stretch your arms out to form a star shape.",
            "Land with feet together and arms back down, bending your knees to land softly.",
            "Repeat with energy — make yourself look like the biggest star in the sky!"
        ],
        tips=["Jump first, then spread — the split happens at the top of the jump.",
              "Land softly with bent knees, not with stiff legs."],
        mistakes=["Spreading before taking off — jump up first, then open out.",
                  "Landing with straight legs — always absorb with bent knees."],
        wt=35, met=5.5, dur=0.7,
        energy_sys="glycolytic", chain="closed", plane=["sagittal","frontal"], ct=["concentric","eccentric"], ci="compound",
        cns="medium", noise="loud", space="medium", stab="medium",
        pres_role="cardio", pres={"sets": 3, "duration_seconds": 20, "rest_seconds": 30},
        rep_secs=1.2,
    ),

    dict(
        id="kids-ex-0014", slug="animal-parade-march", name="Animal Parade March",
        desc="A games-based movement game where children march while imitating different animals on a signal — transitioning between high-knee marching, waddling, slithering, and stomping to build variety of movement patterns and listening skills.",
        focus="Coordination", pm=["quads","glutes"], sm=["core","calves"], st=[],
        sub=["hip flexors"], mp="locomotion", family="games-based-movement",
        dr=1, roles=["warmup","main"], bands=KIDS_ONLY, mt="cardio", diff="beginner", struct="main",
        goals=["improve_coordination","improve_cardio","home_workout","improve_balance"],
        tags=["low_impact","beginner_friendly","kids_friendly","games_based","fun","listening_skills"],
        form=[
            "Start by marching on the spot with high knees.",
            "When the leader calls 'ELEPHANT!' — hinge forward and swing your arms like a trunk.",
            "When they call 'PENGUIN!' — squeeze elbows to sides and waddle.",
            "When they call 'FROG!' — squat down and hop forward.",
            "When they call 'SNAKE!' — lie down and slither along the floor.",
            "Keep swapping animals for 2–3 minutes — listen carefully!"
        ],
        tips=["Change animals quickly — speed of reaction is part of the game.",
              "Really commit to each animal with your whole body."],
        mistakes=["Only moving the arms but not the whole body.",
                  "Ignoring the legs — animal marching should always involve the lower body too."],
        wt=35, met=4.5, dur=2.0,
        energy_sys="glycolytic", chain="closed", plane=["sagittal","frontal"], ct=["concentric","eccentric"], ci="compound",
        cns="medium", noise="loud", space="medium", stab="medium",
        pres_role="cardio", pres={"sets": 1, "duration_seconds": 120, "rest_seconds": 30},
    ),

    dict(
        id="kids-ex-0015", slug="tightrope-walk", name="Tightrope Walk",
        desc="A balance and proprioception exercise where children walk heel-to-toe in a straight line as if on a tightrope, developing foot-eye coordination, ankle stability, and body control.",
        focus="Balance", pm=["calves","core"], sm=["glutes","hip_abductors"], st=["ankles"],
        sub=["peroneus longus","tibialis anterior","gluteus medius"], mp="locomotion", family="balance-challenges",
        dr=1, roles=["warmup","main"], bands=KIDS_ONLY, mt="mobility", diff="beginner", struct="main",
        goals=["improve_balance","improve_coordination","home_workout"],
        tags=["low_impact","beginner_friendly","kids_friendly","balance","fun","proprioception"],
        form=[
            "Find a real or imaginary line on the floor.",
            "Stand at one end and stretch your arms out to the sides for balance.",
            "Take a step placing your right heel directly in front of your left toes.",
            "Then step your left heel in front of your right toes.",
            "Walk in a slow, controlled heel-to-toe line for 5–8 metres without stepping off the line.",
            "Look ahead at a point on the wall, not down at your feet."
        ],
        tips=["Outstretched arms act like a tightrope walker's pole — use them!",
              "Fix your gaze ahead, not on your feet, for better balance."],
        mistakes=["Walking too fast — slow and controlled is the goal.",
                  "Looking down at the feet — this disrupts vestibular balance."],
        wt=35, met=2.2, dur=0.8,
        energy_sys="phosphagen", chain="closed", plane=["sagittal"], ct=["isometric","concentric"], ci="compound",
        cns="low", noise="quiet", space="medium", stab="high",
        pres_role="mobility", pres={"sets": 3, "reps": 1, "rest_seconds": 15, "tempo": "slow"},
    ),

    # ── COORDINATION & GAMES – Kids + Tweens ─────────────────────────────────
    dict(
        id="kids-ex-0016", slug="hopscotch-jump-pattern", name="Hopscotch Jump Pattern",
        desc="A classic playground jump drill adapted as a structured drill — children jump in a 1-1-2 foot pattern (one foot, one foot, two feet) repeatedly, building coordination, rhythm, and single-leg landing mechanics.",
        focus="Coordination", pm=["quads","calves"], sm=["glutes","core"], st=["ankles"],
        sub=["tibialis anterior","gastrocnemius"], mp="plyometric", family="jumping-games",
        dr=1, roles=["warmup","main"], bands=BOTH, mt="cardio", diff="beginner", struct="main",
        goals=["improve_coordination","improve_balance","home_workout","improve_power"],
        tags=["low_impact","beginner_friendly","kids_friendly","games_based","plyometric","fun"],
        form=[
            "Imagine or draw a hopscotch grid: boxes numbered 1–9 in a line.",
            "Hop on your right foot onto box 1, then left foot onto box 2.",
            "When you reach two side-by-side boxes, land with one foot in each (two feet).",
            "Continue hopping to the end, then turn and hop back.",
            "Try to land cleanly and softly in each square."
        ],
        tips=["Keep your arms out for balance on the single-leg hops.",
              "Land toe-to-heel on each hop to absorb impact softly."],
        mistakes=["Landing with stiff legs — always absorb with a bent knee.",
                  "Stepping instead of hopping — commit to a true hop on each foot."],
        wt=40, met=5.0, dur=1.0,
        energy_sys="glycolytic", chain="closed", plane=["sagittal","frontal"], ct=["concentric","eccentric"], ci="compound",
        cns="medium", noise="moderate", space="medium", stab="medium",
        pres_role="cardio", pres={"sets": 3, "reps": 4, "rest_seconds": 30},
        rep_secs=5.0,
    ),

    dict(
        id="kids-ex-0017", slug="skipping-in-place", name="Skipping in Place",
        desc="A rhythmic coordination and cardio drill where children perform the arm and leg pattern of skipping without moving forward — great for coordination timing, calf strength, and getting the heart pumping.",
        focus="Cardio", pm=["calves","quads"], sm=["core","shoulders"], st=["ankles"],
        sub=["gastrocnemius","soleus","hip flexors"], mp="locomotion", family="jumping-games",
        dr=1, roles=["warmup","main"], bands=BOTH, mt="cardio", diff="beginner", struct="warmup",
        goals=["improve_coordination","improve_cardio","home_workout"],
        tags=["low_impact","beginner_friendly","kids_friendly","cardio","fun","no_space_needed"],
        form=[
            "Stand with feet together and arms relaxed.",
            "Hop on your right foot, bringing your left knee up — swing your left arm forward.",
            "Hop on your left foot, bringing your right knee up — swing your right arm forward.",
            "Find a rhythm: hop-hop-hop, like you're skipping but staying in one spot.",
            "Try to keep a steady beat — count 1-2-1-2 to stay in rhythm."
        ],
        tips=["Think of swinging your arms like you're holding a skipping rope — the arm swing drives the rhythm.",
              "Stay on the balls of your feet to keep the movement light and bouncy."],
        mistakes=["Skipping flat-footed — stay on the toes for the true skipping feel.",
                  "Losing the arm-leg coordination — opposite arm and leg always move together."],
        wt=40, met=6.0, dur=1.0,
        energy_sys="glycolytic", chain="closed", plane=["sagittal"], ct=["concentric","eccentric"], ci="compound",
        cns="low", noise="moderate", space="low", stab="medium",
        pres_role="cardio", pres={"sets": 3, "duration_seconds": 30, "rest_seconds": 30},
        rep_secs=0.5,
    ),

    dict(
        id="kids-ex-0018", slug="speed-bounce", name="Speed Bounce",
        desc="A rapid two-footed side-to-side bouncing drill performed continuously over an imaginary or physical low line — building reactive foot speed, coordination, and cardiovascular fitness.",
        focus="Cardio", pm=["calves","quads"], sm=["glutes","core"], st=["ankles"],
        sub=["gastrocnemius","soleus","peroneus longus"], mp="plyometric", family="lateral-jumps",
        dr=2, roles=["warmup","main"], bands=BOTH, mt="cardio", diff="beginner", struct="main",
        goals=["improve_coordination","improve_cardio","home_workout","improve_power"],
        tags=["low_impact","beginner_friendly","kids_friendly","cardio","plyometric","speed"],
        form=[
            "Place a piece of tape or imagine a line on the floor.",
            "Stand with feet together on one side of the line.",
            "Bounce quickly side to side over the line with both feet together, as fast as you can.",
            "Keep jumps low — speed matters more than height.",
            "Count how many times you cross the line in 20 seconds and try to beat your score!"
        ],
        tips=["Stay on the balls of your feet — flat-footed bouncing slows you down.",
              "Look straight ahead, not at your feet."],
        mistakes=["Jumping too high — keep ground contact time short.",
                  "Landing with stiff legs — stay springy and soft in the knees."],
        wt=40, met=6.5, dur=0.5,
        energy_sys="glycolytic", chain="closed", plane=["frontal"], ct=["concentric","eccentric"], ci="compound",
        cns="medium", noise="moderate", space="low", stab="medium",
        pres_role="cardio", pres={"sets": 3, "duration_seconds": 20, "rest_seconds": 30},
        rep_secs=0.4,
    ),

    dict(
        id="kids-ex-0019", slug="freeze-dance-sprint", name="Freeze Dance Sprint",
        desc="A games-based cardio and reaction exercise where children sprint or run on the spot until a signal is given, then freeze completely still — training aerobic capacity, reaction time, and body control.",
        focus="Cardio", pm=["quads","calves","glutes"], sm=["core","hamstrings"], st=[],
        sub=["hip flexors","gastrocnemius"], mp="locomotion", family="games-based-movement",
        dr=1, roles=["warmup","main"], bands=BOTH, mt="cardio", diff="beginner", struct="main",
        goals=["improve_coordination","improve_cardio","home_workout","improve_reaction"],
        tags=["low_impact","beginner_friendly","kids_friendly","games_based","cardio","fun","reaction"],
        form=[
            "Find an open space or run on the spot.",
            "Sprint or run fast until the leader shouts 'FREEZE!'",
            "Immediately stop in any position and hold still — don't wobble!",
            "Hold the freeze for 3–5 seconds until the leader says 'GO!'",
            "Then sprint again. Repeat for 2–3 minutes."
        ],
        tips=["The quicker you freeze, the better — train your brain to stop fast.",
              "Freeze in a fun pose to make it more fun — can you balance on one foot?"],
        mistakes=["Shuffling after the freeze — the goal is instant stillness.",
                  "Slowing down before the freeze — keep the effort high until the signal."],
        wt=40, met=7.0, dur=2.0,
        energy_sys="glycolytic", chain="closed", plane=["sagittal"], ct=["concentric","eccentric","isometric"], ci="compound",
        cns="medium", noise="loud", space="medium", stab="medium",
        pres_role="cardio", pres={"sets": 1, "duration_seconds": 120, "rest_seconds": 30},
    ),

    dict(
        id="kids-ex-0020", slug="high-knee-stomp-march", name="High Knee Stomp March",
        desc="An exaggerated marching drill where children lift their knees up high with each slow, deliberate stomp — developing hip flexor strength, single-leg balance, and a fun sense of marching rhythm.",
        focus="Coordination", pm=["quads","hip_flexors"], sm=["core","glutes"], st=["calves"],
        sub=["iliopsoas","rectus femoris"], mp="locomotion", family="marching-drills",
        dr=1, roles=["warmup","main"], bands=BOTH, mt="cardio", diff="beginner", struct="warmup",
        goals=["improve_coordination","improve_cardio","home_workout","improve_balance"],
        tags=["low_impact","beginner_friendly","kids_friendly","warmup","fun"],
        form=[
            "Stand tall with feet hip-width apart, arms bent at 90 degrees like a soldier.",
            "Lift your right knee up as high as your hip — stomp it back down loudly.",
            "Then lift your left knee up high — stomp it back down.",
            "March forward or on the spot, swinging the opposite arm with each step.",
            "Exaggerate every movement — make it big and bold!"
        ],
        tips=["Drive the knee up using your hip flexors, not just lifting the foot.",
              "Swing the opposite arm forward with each knee lift for rhythm."],
        mistakes=["Leaning back — keep your torso upright and core braced.",
                  "Making tiny knee lifts — the whole point is to go HIGH!"],
        wt=40, met=4.5, dur=1.0,
        energy_sys="glycolytic", chain="closed", plane=["sagittal"], ct=["concentric","eccentric"], ci="compound",
        cns="low", noise="loud", space="low", stab="medium",
        pres_role="cardio", pres={"sets": 3, "duration_seconds": 30, "rest_seconds": 20},
        rep_secs=1.0,
    ),

    dict(
        id="kids-ex-0021", slug="lateral-hop", name="Lateral Hop",
        desc="A single-leg lateral jumping drill where children push off one foot to hop sideways, landing on the same foot — developing unilateral leg power, landing mechanics, and lateral athleticism.",
        focus="Power", pm=["glutes","quads","calves"], sm=["core","hip_abductors"], st=["ankles"],
        sub=["gluteus medius","peroneus longus"], mp="plyometric", family="lateral-jumps",
        dr=2, roles=["main"], bands=BOTH, mt="cardio", diff="beginner", struct="main",
        goals=["improve_coordination","improve_power","improve_balance","home_workout"],
        tags=["low_impact","beginner_friendly","kids_friendly","plyometric","lateral"],
        form=[
            "Stand on your right foot with a slight knee bend.",
            "Push off to the left and land softly on your left foot, absorbing with a bent knee.",
            "Hold the landing for 1 second to check your balance.",
            "Then push back to the right, landing on your right foot.",
            "Start small and slow, then build speed as you get confident."
        ],
        tips=["Land on the middle of your foot (not just the toes) to absorb impact safely.",
              "Keep the knee of the landing leg in line with your toes — don't let it collapse inward."],
        mistakes=["Landing with a straight, stiff leg — always absorb with a bent knee.",
                  "Rushing — pause on each landing to build the balance skill."],
        wt=40, met=5.5, dur=0.8,
        energy_sys="phosphagen", chain="closed", plane=["frontal"], ct=["concentric","eccentric"], ci="compound",
        cns="medium", noise="moderate", space="medium", stab="high",
        per_side=True, uni=True,
        pres_role="strength", pres={"sets": 3, "reps": 6, "rest_seconds": 30, "tempo": "controlled"},
        rep_secs=2.0,
    ),

    dict(
        id="kids-ex-0022", slug="arm-circles-kids", name="Arm Circles",
        desc="A large, expressive shoulder warm-up where children extend their arms fully and make big forward and backward circles — mobilising the shoulder joint and increasing blood flow to the upper body.",
        focus="Flexibility", pm=["shoulders"], sm=["back","chest"], st=[],
        sub=["rotator cuff","deltoids","scapular stabilisers"], mp="mobility", family="shoulder-mobility",
        dr=1, roles=["warmup"], bands=BOTH, mt="mobility", diff="beginner", struct="warmup",
        goals=["improve_mobility","improve_flexibility","home_workout","warmup"],
        tags=["low_impact","beginner_friendly","kids_friendly","warmup","shoulder_mobility"],
        form=[
            "Stand with feet shoulder-width apart and extend both arms out to the sides like aeroplane wings.",
            "Make big, slow circles in a forward direction — try to make them as big as possible.",
            "Do 10 forward circles, then reverse direction for 10 backward circles.",
            "Keep the arms fully extended and the movement smooth and controlled."
        ],
        tips=["Make the circles as big as you can — engage the whole shoulder, not just the wrist.",
              "Keep your torso still and upright — only the arms should move."],
        mistakes=["Making tiny wrist circles — the movement should be from the shoulder joint.",
                  "Bending the elbows — keep arms straight to get the full range of motion."],
        wt=40, met=2.0, dur=0.5,
        energy_sys="phosphagen", chain="open", plane=["sagittal","transverse"], ct=["concentric","eccentric"], ci="isolation",
        cns="low", noise="quiet", space="low", stab="low",
        pres_role="mobility", pres={"sets": 2, "reps": 10, "rest_seconds": 15, "tempo": "controlled"},
        rep_secs=2.0,
    ),

    dict(
        id="kids-ex-0023", slug="hip-circle", name="Hip Circle",
        desc="A hip mobility warm-up drill where children place hands on their hips and make large circles with their pelvis, like hula-hooping without a hoop — loosening hip joints and improving lumbar mobility.",
        focus="Flexibility", pm=["glutes","hip_flexors"], sm=["core","back"], st=[],
        sub=["hip external rotators","iliac crest","lumbar erectors"], mp="mobility", family="hip-mobility",
        dr=1, roles=["warmup"], bands=BOTH, mt="mobility", diff="beginner", struct="warmup",
        goals=["improve_mobility","improve_flexibility","home_workout","warmup"],
        tags=["low_impact","beginner_friendly","kids_friendly","warmup","hip_mobility","fun"],
        form=[
            "Stand with feet hip-width apart and hands on your hips.",
            "Push your hips to the right, then back, then left, then forward.",
            "Make the circle as big and smooth as possible — like you're hula-hooping.",
            "Complete 8–10 circles in one direction, then reverse for 8–10 the other way.",
            "Keep your shoulders still and let only your hips move."
        ],
        tips=["Make the circle slow and deliberate — rushing misses the mobility benefit.",
              "Try to trace the biggest circle you can with your hip bones."],
        mistakes=["Moving the whole upper body instead of just the hips.",
                  "Making tiny movements — go for maximum range of motion."],
        wt=40, met=2.2, dur=0.5,
        energy_sys="phosphagen", chain="open", plane=["transverse","frontal"], ct=["concentric","eccentric"], ci="isolation",
        cns="low", noise="quiet", space="low", stab="low",
        pres_role="mobility", pres={"sets": 2, "reps": 10, "rest_seconds": 15, "tempo": "slow"},
        rep_secs=2.5,
    ),

    dict(
        id="kids-ex-0024", slug="diagonal-jump", name="Diagonal Jump",
        desc="A multi-directional plyometric drill where children jump at diagonal angles — forward-right, forward-left — developing change-of-direction power, coordination, and spatial awareness.",
        focus="Coordination", pm=["quads","glutes","calves"], sm=["core","hip_abductors"], st=["ankles"],
        sub=["gastrocnemius","gluteus medius"], mp="plyometric", family="jumping-games",
        dr=2, roles=["main"], bands=BOTH, mt="cardio", diff="beginner", struct="main",
        goals=["improve_coordination","improve_power","home_workout","improve_agility"],
        tags=["low_impact","beginner_friendly","kids_friendly","plyometric","agility","multi_directional"],
        form=[
            "Stand with feet hip-width apart, facing forward.",
            "Jump diagonally to the forward-right, landing softly on both feet.",
            "From there, jump diagonally forward-left.",
            "Continue zigzagging forward in diagonal jumps for 4–6 jumps.",
            "Turn around and diagonal-jump your way back."
        ],
        tips=["Point your landing toes in the direction you're jumping — it helps with body rotation.",
              "Land softly with bent knees each time."],
        mistakes=["Only jumping straight forward — make sure the angle is truly diagonal.",
                  "Stiff leg landing — always absorb the jump with bent knees."],
        wt=40, met=5.5, dur=0.8,
        energy_sys="phosphagen", chain="closed", plane=["sagittal","frontal"], ct=["concentric","eccentric"], ci="compound",
        cns="medium", noise="moderate", space="medium", stab="medium",
        pres_role="cardio", pres={"sets": 3, "reps": 6, "rest_seconds": 30},
        rep_secs=1.5,
    ),

    dict(
        id="kids-ex-0025", slug="single-leg-balance-challenge", name="Single Leg Balance Challenge",
        desc="A progressively harder balance challenge where children hold a single-leg stand and attempt increasingly difficult tasks — eyes closed, reaching forward, or catching a ball — building proprioception and concentration.",
        focus="Balance", pm=["calves","glutes"], sm=["core","hip_abductors"], st=["ankles"],
        sub=["gluteus medius","tibialis anterior","soleus"], mp="hold", family="balance-challenges",
        dr=1, roles=["warmup","main"], bands=BOTH, mt="mobility", diff="beginner", struct="main",
        goals=["improve_balance","improve_coordination","home_workout"],
        tags=["low_impact","beginner_friendly","kids_friendly","balance","proprioception"],
        form=[
            "Stand on your right foot with your knee slightly bent.",
            "Level 1: Hold for 10 seconds with eyes open.",
            "Level 2: Hold with eyes closed for 10 seconds.",
            "Level 3: While balancing, reach forward with both arms and hold.",
            "Switch to the left foot and repeat all three levels.",
            "Track your best time on each level!"
        ],
        tips=["Spread your toes wide to create a bigger stable base on the standing foot.",
              "Fix your gaze on a still point when eyes are open — it helps a lot."],
        mistakes=["Gripping the toes — relax the foot and use the whole sole.",
                  "Skipping straight to eyes closed — build up through the levels."],
        wt=40, met=2.0, dur=0.5,
        energy_sys="phosphagen", chain="closed", plane=["frontal"], ct=["isometric"], ci="isolation",
        cns="low", noise="quiet", space="low", stab="high",
        per_side=True, uni=True,
        is_hold=True, hold_secs=10,
        pres_role="mobility", pres={"sets": 3, "duration_seconds": 10, "rest_seconds": 15, "tempo": "static"},
        rep_secs=10.0,
    ),

    dict(
        id="kids-ex-0026", slug="reaction-jump-drill", name="Reaction Jump Drill",
        desc="A cognitive-motor drill where children jump in different directions based on colour cards, hand signals, or verbal cues — training reaction time, decision-making, and explosive movement simultaneously.",
        focus="Coordination", pm=["quads","calves","glutes"], sm=["core"], st=["ankles"],
        sub=["gastrocnemius","hip flexors"], mp="plyometric", family="games-based-movement",
        dr=2, roles=["warmup","main"], bands=BOTH, mt="cardio", diff="beginner", struct="main",
        goals=["improve_coordination","improve_reaction","home_workout","improve_cardio"],
        tags=["low_impact","beginner_friendly","kids_friendly","games_based","reaction","fun","cognitive"],
        form=[
            "Stand in a ready position: feet hip-width, knees slightly bent, weight on toes.",
            "A coach or partner calls a direction: 'FORWARD', 'BACK', 'LEFT', or 'RIGHT'.",
            "Jump immediately in that direction with both feet and land softly.",
            "Reset to the starting position and wait for the next call.",
            "Calls get faster each round — can you keep up?"
        ],
        tips=["Stay on the balls of your feet in the ready position so you can react faster.",
              "Jump the moment you hear the word — don't wait to think about it."],
        mistakes=["Flat-footed stance — you need to be light on your feet to react quickly.",
                  "Hesitating — trust your instinct and jump!"],
        wt=40, met=6.0, dur=1.0,
        energy_sys="phosphagen", chain="closed", plane=["sagittal","frontal","transverse"], ct=["concentric","eccentric"], ci="compound",
        cns="high", noise="moderate", space="medium", stab="medium",
        pres_role="cardio", pres={"sets": 3, "duration_seconds": 30, "rest_seconds": 30},
        rep_secs=1.0,
    ),

    dict(
        id="kids-ex-0027", slug="balance-walk-line", name="Balance Walk Line",
        desc="A slow, deliberate walking drill where children walk along a painted or taped straight line placing each foot precisely heel-to-toe, developing proprioception, ankle stability, and spatial discipline.",
        focus="Balance", pm=["core","calves"], sm=["glutes","hip_abductors"], st=["ankles"],
        sub=["peroneus longus","tibialis anterior"], mp="locomotion", family="balance-challenges",
        dr=1, roles=["warmup","main"], bands=BOTH, mt="mobility", diff="beginner", struct="main",
        goals=["improve_balance","improve_coordination","home_workout"],
        tags=["low_impact","beginner_friendly","kids_friendly","balance","proprioception","no_equipment"],
        form=[
            "Use a piece of tape, a painted line, or just imagine a line on the floor.",
            "Stand at one end and fix your gaze 2 metres ahead on the line.",
            "Step your right heel directly in front of your left toes, touching heel to toe.",
            "Step your left heel in front of your right toes — heel to toe.",
            "Walk the full length of the line (5–10 m) without stepping off.",
            "Turn around and walk back."
        ],
        tips=["Arms out to the sides work like a balancing pole — use them.",
              "Look ahead, not at your feet — use your peripheral vision for the line."],
        mistakes=["Rushing the walk — slow is better than fast and wobbly.",
                  "Watching your feet — eyes should stay ahead."],
        wt=40, met=2.2, dur=0.8,
        energy_sys="phosphagen", chain="closed", plane=["sagittal"], ct=["isometric","concentric"], ci="compound",
        cns="low", noise="quiet", space="medium", stab="high",
        pres_role="mobility", pres={"sets": 3, "reps": 1, "rest_seconds": 15, "tempo": "slow"},
    ),

    dict(
        id="kids-ex-0028", slug="crab-walk-and-reach", name="Crab Walk and Reach",
        desc="A dynamic variation of the crab walk where children pause mid-crawl to lift one arm and reach toward the ceiling — building shoulder stability, core rotation, and coordination in a fun ground-based drill.",
        focus="Coordination", pm=["shoulders","core","glutes"], sm=["triceps","back"], st=["wrists","ankles"],
        sub=["rotator cuff","obliques","gluteus maximus"], mp="locomotion", family="ground-movement",
        dr=2, roles=["main"], bands=BOTH, mt="strength", diff="beginner", struct="main",
        goals=["improve_coordination","build_core","build_upper_body","home_workout"],
        tags=["low_impact","beginner_friendly","kids_friendly","games_based","upper_body","core","fun"],
        form=[
            "Sit on the floor, place hands behind you and lift your hips to create a reverse table-top.",
            "Walk sideways — two steps to the right.",
            "Pause, then lift your left arm up and point it at the ceiling. Hold 2 seconds.",
            "Lower the arm, walk two steps to the right, then lift the right arm.",
            "Continue alternating reaches as you travel sideways."
        ],
        tips=["Press through your heels and hands equally to keep hips high.",
              "When you reach up, rotate your chest open — look at your raised hand."],
        mistakes=["Letting hips sag — keep them lifted throughout.",
                  "Rushing the reach — hold it long enough to feel the rotation."],
        wt=40, met=4.0, dur=0.8,
        energy_sys="glycolytic", chain="closed", plane=["sagittal","transverse"], ct=["concentric","isometric"], ci="compound",
        cns="medium", noise="quiet", space="medium", stab="medium",
        per_side=True,
        pres_role="strength", pres={"sets": 2, "reps": 8, "rest_seconds": 40, "tempo": "controlled"},
        rep_secs=4.0,
    ),

    dict(
        id="kids-ex-0029", slug="dynamic-jump-and-stick", name="Dynamic Jump and Stick",
        desc="A jump-landing mechanics exercise where children jump from two feet and attempt to land perfectly balanced and still — teaching safe landing technique and deceleration control.",
        focus="Power", pm=["quads","glutes","calves"], sm=["core","hamstrings"], st=["ankles"],
        sub=["gluteus maximus","gastrocnemius","tibialis anterior"], mp="plyometric", family="jumping-games",
        dr=2, roles=["main"], bands=BOTH, mt="cardio", diff="beginner", struct="main",
        goals=["improve_coordination","improve_power","improve_balance","home_workout"],
        tags=["low_impact","beginner_friendly","kids_friendly","plyometric","landing_mechanics"],
        form=[
            "Stand with feet hip-width apart.",
            "Bend your knees and jump forward, upward, or from a small step.",
            "When you land, freeze completely still in a balanced athletic position.",
            "Hold the landing for 3 seconds — check that: knees are over toes, chest is up, you're not wobbling.",
            "If you wobble, try again — the goal is a perfect 'stick' landing."
        ],
        tips=["Think 'quiet feet' — the softer the landing sound, the better your technique.",
              "Land mid-foot, not on toes or heels, and roll down through the foot."],
        mistakes=["Landing stiff-legged — you need 30–45 degrees of knee bend to absorb safely.",
                  "Not freezing on landing — if you keep moving, you can't assess the quality."],
        wt=40, met=5.5, dur=0.8,
        energy_sys="phosphagen", chain="closed", plane=["sagittal"], ct=["concentric","eccentric"], ci="compound",
        cns="medium", noise="moderate", space="medium", stab="high",
        pres_role="strength", pres={"sets": 3, "reps": 6, "rest_seconds": 30, "tempo": "controlled"},
        rep_secs=3.0,
    ),

    dict(
        id="kids-ex-0030", slug="mirror-movement-drill", name="Mirror Movement Drill",
        desc="A partner-based (or solo shadow-form) coordination game where one child mirrors the exact movements of the leader in real time — training reactive movement, spatial awareness, and focus.",
        focus="Coordination", pm=["quads","calves","glutes"], sm=["core"], st=[],
        sub=["hip flexors"], mp="locomotion", family="games-based-movement",
        dr=1, roles=["warmup","main"], bands=BOTH, mt="cardio", diff="beginner", struct="main",
        goals=["improve_coordination","improve_reaction","improve_cardio","home_workout"],
        tags=["low_impact","beginner_friendly","kids_friendly","games_based","reaction","partner","cognitive","fun"],
        form=[
            "Stand facing your partner (or a mirror) about 1 metre apart.",
            "The leader moves slowly — stepping sideways, raising an arm, squatting slightly.",
            "The mirror must copy every movement simultaneously with no delay.",
            "After 45 seconds, swap who is the leader.",
            "Try to make transitions so smooth an observer can't tell who's leading!"
        ],
        tips=["Leaders: start slow with big, obvious moves and gradually speed up.",
              "Mirrors: don't anticipate — truly react to what you see."],
        mistakes=["Leaders moving too fast too soon — build tempo gradually.",
                  "Mirrors looking away from the leader — maintain eye contact."],
        wt=40, met=4.5, dur=1.5,
        energy_sys="glycolytic", chain="closed", plane=["sagittal","frontal"], ct=["concentric","eccentric","isometric"], ci="compound",
        cns="high", noise="moderate", space="medium", stab="medium",
        pres_role="cardio", pres={"sets": 2, "duration_seconds": 45, "rest_seconds": 30},
    ),

    # ── BASIC STRENGTH & STABILITY – Tweens only ──────────────────────────────
    dict(
        id="kids-ex-0031", slug="wall-sit", name="Wall Sit",
        desc="An isometric lower-body strength exercise where tweens slide their back down a wall until thighs are parallel to the floor and hold the position — building quad endurance, glute activation, and mental toughness.",
        focus="Strength", pm=["quads"], sm=["glutes","hamstrings"], st=["core"],
        sub=["rectus femoris","vastus medialis","gluteus maximus"], mp="hold", family="isometric-holds",
        dr=2, roles=["main"], bands=TWEENS_ONLY, mt="strength", diff="beginner", struct="main",
        goals=["build_legs","improve_endurance","home_workout"],
        tags=["low_impact","beginner_friendly","no_equipment","isometric","strength"],
        form=[
            "Stand with your back flat against a wall and feet about 60 cm away.",
            "Slide your back down the wall until your thighs are parallel to the floor — like sitting in an invisible chair.",
            "Ensure your knees are directly above your ankles — not forward past your toes.",
            "Press your whole back flat into the wall.",
            "Hold for as long as you can, building up to 30–60 seconds."
        ],
        tips=["Press your lower back into the wall — don't let it arch away.",
              "Breathe steadily — hold your breath and you'll tire faster."],
        mistakes=["Thighs not parallel — you need at least 90 degrees at the knee.",
                  "Knees drifting inward — keep them tracking over your second toe."],
        wt=45, met=3.5, dur=0.8,
        energy_sys="phosphagen", chain="closed", plane=["sagittal"], ct=["isometric"], ci="isolation",
        cns="low", noise="quiet", space="low", stab="low",
        is_hold=True, hold_secs=30,
        pres_role="strength", pres={"sets": 3, "duration_seconds": 30, "rest_seconds": 45, "tempo": "static"},
        rep_secs=30.0,
    ),

    dict(
        id="kids-ex-0032", slug="hip-bridge-kids", name="Hip Bridge",
        desc="A foundational glute and posterior chain exercise where tweens lie on their back, plant their feet, and drive their hips up to form a straight line from knees to shoulders — essential for athletic hip extension.",
        focus="Strength", pm=["glutes"], sm=["hamstrings","core"], st=["back"],
        sub=["gluteus maximus","hamstring distal","erector spinae"], mp="hip_extension", family="glute-bridges",
        dr=1, roles=["warmup","main"], bands=TWEENS_ONLY, mt="strength", diff="beginner", struct="main",
        goals=["build_legs","build_glutes","improve_posture","home_workout"],
        tags=["low_impact","beginner_friendly","no_equipment","glutes","strength"],
        form=[
            "Lie on your back with knees bent and feet flat on the floor, hip-width apart.",
            "Place your arms at your sides with palms flat on the floor.",
            "Squeeze your glutes and push your hips up toward the ceiling.",
            "Stop when your body forms a straight line from knees to shoulders.",
            "Hold for 2 seconds at the top, then slowly lower back down."
        ],
        tips=["Squeeze your glutes hard at the top — that's where the exercise works.",
              "Don't push your hips too high — a straight line from knees to shoulders is the target."],
        mistakes=["Hyperextending the lower back at the top — keep a neutral spine.",
                  "Letting knees cave inward — keep them hip-width apart throughout."],
        wt=45, met=3.0, dur=1.0,
        energy_sys="phosphagen", chain="closed", plane=["sagittal"], ct=["concentric","eccentric","isometric"], ci="compound",
        cns="low", noise="quiet", space="low", stab="low",
        pres_role="strength", pres={"sets": 3, "reps": 12, "rest_seconds": 30, "tempo": "controlled"},
        rep_secs=3.0,
    ),

    dict(
        id="kids-ex-0033", slug="hip-bridge-march-kids", name="Hip Bridge March",
        desc="A dynamic progression of the hip bridge where tweens hold the bridge position and alternate lifting each foot off the floor in a marching pattern — challenging core stability, glute endurance, and hip control.",
        focus="Strength", pm=["glutes","core"], sm=["hamstrings","hip_flexors"], st=["back"],
        sub=["gluteus maximus","obliques","erector spinae"], mp="hip_extension", family="glute-bridges",
        dr=2, roles=["main"], bands=TWEENS_ONLY, mt="strength", diff="beginner", struct="main",
        goals=["build_glutes","build_core","improve_balance","home_workout"],
        tags=["low_impact","beginner_friendly","no_equipment","glutes","core","stability"],
        form=[
            "Perform a Hip Bridge and hold the top position.",
            "Lift your right foot off the floor and bring your right knee toward your chest.",
            "Hold for 2 seconds, then lower the right foot back down.",
            "Repeat on the left side.",
            "Keep your hips level throughout — don't let one side drop."
        ],
        tips=["Think of a table with one leg lifted — the table top (your hips) must stay perfectly flat.",
              "Squeeze the standing-leg glute harder when the other foot lifts."],
        mistakes=["Letting the hip on the lifted-leg side drop — fight to keep hips level.",
                  "Rushing the march — slow, deliberate lifts train stability better."],
        wt=45, met=3.5, dur=1.0,
        energy_sys="phosphagen", chain="closed", plane=["sagittal","frontal"], ct=["concentric","isometric"], ci="compound",
        cns="medium", noise="quiet", space="low", stab="high",
        per_side=True,
        pres_role="strength", pres={"sets": 3, "reps": 10, "rest_seconds": 30, "tempo": "controlled"},
        rep_secs=4.0,
    ),

    dict(
        id="kids-ex-0034", slug="skater-hop-kids", name="Skater Hop",
        desc="A lateral plyometric drill where tweens bound side to side on alternating feet like a speed skater, developing unilateral leg power, lateral stability, and cardiovascular capacity.",
        focus="Power", pm=["glutes","quads","calves"], sm=["core","hip_abductors"], st=["ankles"],
        sub=["gluteus medius","gastrocnemius","peroneus longus"], mp="plyometric", family="lateral-jumps",
        dr=2, roles=["main"], bands=TWEENS_ONLY, mt="cardio", diff="beginner", struct="main",
        goals=["improve_power","improve_coordination","improve_cardio","home_workout"],
        tags=["low_impact","beginner_friendly","plyometric","lateral","cardio","athletic"],
        form=[
            "Stand on your right foot with a slight knee bend.",
            "Push off to the left, crossing your left foot in a wide lateral bound.",
            "Land on your left foot, right foot trailing behind — like a speed skater's glide.",
            "Immediately push off left to bound back to the right.",
            "Swing the opposite arm forward with each bound for power and balance."
        ],
        tips=["Land on the front-outside of your foot and absorb with a bent knee.",
              "Reach the trailing foot behind and across to increase the glide length."],
        mistakes=["Landing with both feet — each landing should be single-leg.",
                  "Neglecting the arm swing — it's key for momentum and balance."],
        wt=45, met=7.0, dur=0.8,
        energy_sys="glycolytic", chain="closed", plane=["frontal"], ct=["concentric","eccentric"], ci="compound",
        cns="medium", noise="moderate", space="medium", stab="high",
        per_side=True, uni=True,
        pres_role="cardio", pres={"sets": 3, "duration_seconds": 20, "rest_seconds": 30},
        rep_secs=0.8,
    ),

    dict(
        id="kids-ex-0035", slug="half-burpee-kids", name="Half Burpee",
        desc="A simplified burpee variation where tweens jump their feet back to a plank and return without the push-up or jump — building core strength, hip flexor power, and cardiovascular conditioning progressively.",
        focus="Cardio", pm=["core","quads","shoulders"], sm=["glutes","calves","chest"], st=["wrists"],
        sub=["hip flexors","rectus abdominis","anterior deltoid"], mp="locomotion", family="burpee-variations",
        dr=2, roles=["main"], bands=TWEENS_ONLY, mt="cardio", diff="beginner", struct="main",
        goals=["improve_cardio","build_core","build_upper_body","home_workout"],
        tags=["low_impact","beginner_friendly","cardio","full_body","no_equipment"],
        form=[
            "Start standing with feet hip-width apart.",
            "Bend down and place your hands on the floor just outside your feet.",
            "Jump or step both feet back to a high plank position.",
            "Hold the plank for one second — keep your core tight.",
            "Jump or step your feet back in toward your hands.",
            "Stand up tall. That is one rep."
        ],
        tips=["If jumping feels too hard, step one foot back then the other — same effect, lower intensity.",
              "Keep your core braced in the plank — don't let your hips sag or pike up."],
        mistakes=["Piking the hips up in the plank — aim for a flat, board-like body.",
                  "Landing with stiff legs when stepping in — absorb with bent knees."],
        wt=45, met=7.5, dur=1.0,
        energy_sys="glycolytic", chain="closed", plane=["sagittal"], ct=["concentric","eccentric"], ci="compound",
        cns="medium", noise="moderate", space="medium", stab="medium",
        pres_role="cardio", pres={"sets": 3, "reps": 8, "rest_seconds": 40, "tempo": "controlled"},
        rep_secs=3.0,
    ),

    dict(
        id="kids-ex-0036", slug="scapula-push-up-raise", name="Scapula Push-Up Raise",
        desc="A shoulder blade mobility and serratus anterior strengthening exercise where tweens in a plank position protract and retract their shoulder blades without bending the elbows — a foundational shoulder health drill for young athletes.",
        focus="Strength", pm=["shoulders"], sm=["chest","core"], st=["wrists"],
        sub=["serratus anterior","rhomboids","subscapularis"], mp="push_horizontal", family="push-up-variations",
        dr=2, roles=["warmup","main"], bands=TWEENS_ONLY, mt="strength", diff="beginner", struct="warmup",
        goals=["build_upper_body","improve_posture","improve_mobility","home_workout"],
        tags=["low_impact","beginner_friendly","shoulder_health","scapular","posture","no_equipment"],
        form=[
            "Start in a high plank with arms straight, hands under shoulders.",
            "Keep your arms STRAIGHT — this is not a push-up.",
            "Allow your shoulder blades to squeeze together (retract) so your chest sinks slightly.",
            "Then push your shoulder blades apart (protract) so your upper back rounds slightly.",
            "Move only through the shoulder blades — arms stay locked straight throughout."
        ],
        tips=["Think of 'spreading your wings' when you protract — push the floor away.",
              "The movement is small — don't bend your elbows even slightly."],
        mistakes=["Bending the elbows — this turns it into a push-up, not a scapula drill.",
                  "Moving through the lower back — isolate the shoulder girdle only."],
        wt=45, met=3.0, dur=0.8,
        energy_sys="phosphagen", chain="closed", plane=["sagittal"], ct=["concentric","eccentric"], ci="isolation",
        cns="low", noise="quiet", space="low", stab="medium",
        tax_sports=["baseball", "tennis", "boxing"],
        pres_role="strength", pres={"sets": 3, "reps": 12, "rest_seconds": 30, "tempo": "controlled"},
        rep_secs=2.0,
    ),

    dict(
        id="kids-ex-0037", slug="lateral-lunge-kids", name="Lateral Lunge",
        desc="A side-stepping lower body strength exercise where tweens step wide to one side and lower their body into a deep lateral lunge — developing adductor flexibility, single-leg strength, and frontal-plane stability.",
        focus="Strength", pm=["quads","glutes"], sm=["hamstrings","adductors"], st=["core","calves"],
        sub=["adductors","gluteus medius","vastus medialis"], mp="squat", family="lunge-variations",
        dr=2, roles=["warmup","main"], bands=TWEENS_ONLY, mt="strength", diff="beginner", struct="main",
        goals=["build_legs","improve_flexibility","improve_balance","home_workout"],
        tags=["low_impact","beginner_friendly","lower_body","lateral","no_equipment"],
        form=[
            "Stand with feet together and hands clasped in front of your chest.",
            "Step your right foot wide out to the side — about double shoulder-width.",
            "Shift your weight to the right, bending the right knee and pushing your hips back.",
            "The right thigh should be close to parallel to the floor; left leg stays straight.",
            "Push off the right foot to return to standing, then repeat on the left side."
        ],
        tips=["Keep your chest up and hinge from the hips — don't just collapse downward.",
              "The straight leg should stretch your inner thigh — lean into that stretch."],
        mistakes=["Letting the lunging knee fall inward — it should track over the second toe.",
                  "Rising too quickly — control the descent and the push-up."],
        wt=45, met=4.5, dur=1.0,
        energy_sys="glycolytic", chain="closed", plane=["frontal"], ct=["concentric","eccentric"], ci="compound",
        cns="low", noise="quiet", space="medium", stab="medium",
        per_side=True, uni=True,
        tax_sports=["basketball", "soccer", "football"],
        pres_role="strength", pres={"sets": 3, "reps": 8, "rest_seconds": 30, "tempo": "controlled"},
        rep_secs=3.0,
    ),

    dict(
        id="kids-ex-0038", slug="speed-skater-kids", name="Speed Skater",
        desc="A continuous lateral bounding drill where tweens bound side to side with a crossover step and an arm swing, mimicking an ice speed skater — developing explosive lateral power and cardiovascular fitness.",
        focus="Power", pm=["glutes","quads"], sm=["calves","core","hip_abductors"], st=["ankles"],
        sub=["gluteus medius","gastrocnemius","peroneus longus"], mp="plyometric", family="lateral-jumps",
        dr=3, roles=["main"], bands=TWEENS_ONLY, mt="cardio", diff="intermediate", struct="main",
        goals=["improve_power","improve_cardio","improve_coordination","home_workout"],
        tags=["intermediate","plyometric","lateral","cardio","athletic","sport_prep"],
        form=[
            "Begin on your right foot, with left foot behind and to the right (cross position).",
            "Push off powerfully to the left, bounding as far as possible.",
            "Land on your left foot and cross the right foot behind.",
            "Swing your arms in a speed-skater motion — opposite arm to opposite foot.",
            "Continue bounding side to side with maximum power."
        ],
        tips=["Drive your arms hard — the arm swing creates momentum.",
              "Try to land on the outside edge of your foot and then roll to flat."],
        mistakes=["Taking small hops instead of long bounds — really drive for distance.",
                  "Neglecting the crossover step — the trailing foot crossing behind is key technique."],
        wt=45, met=8.0, dur=1.0,
        energy_sys="glycolytic", chain="closed", plane=["frontal","transverse"], ct=["concentric","eccentric"], ci="compound",
        cns="high", noise="moderate", space="medium", stab="high",
        per_side=True, uni=True,
        pres_role="cardio", pres={"sets": 3, "duration_seconds": 20, "rest_seconds": 40},
        rep_secs=0.7,
    ),

    dict(
        id="kids-ex-0039", slug="t-balance-reach", name="T-Balance Reach",
        desc="A hip hinge balance challenge where tweens stand on one leg, hinge forward to horizontal, and extend the opposite leg behind them forming a T-shape — building posterior chain strength and single-leg stability.",
        focus="Balance", pm=["glutes","hamstrings"], sm=["core","back"], st=["calves","ankles"],
        sub=["gluteus maximus","erector spinae","semimembranosus"], mp="hold", family="balance-challenges",
        dr=2, roles=["main"], bands=TWEENS_ONLY, mt="strength", diff="beginner", struct="main",
        goals=["improve_balance","build_legs","improve_flexibility","home_workout"],
        tags=["low_impact","beginner_friendly","balance","proprioception","posterior_chain","hip_hinge"],
        form=[
            "Stand on your right foot with a slight knee bend.",
            "Hinge forward from your hips, extending your left leg behind you.",
            "Reach both arms forward or keep them wide for balance.",
            "Continue until your body and left leg form a horizontal T-shape.",
            "Hold for 3–5 seconds, return to standing, then switch legs."
        ],
        tips=["Keep the hips level — both hip bones should point straight down to the floor.",
              "Maintain a neutral spine — don't round the lower back as you hinge."],
        mistakes=["Rotating the hip of the lifted leg — keep both hips facing down.",
                  "Locking the standing knee — keep a soft bend in it throughout."],
        wt=45, met=2.8, dur=0.8,
        energy_sys="phosphagen", chain="closed", plane=["sagittal"], ct=["isometric"], ci="compound",
        cns="medium", noise="quiet", space="low", stab="high",
        per_side=True, uni=True,
        is_hold=True, hold_secs=5,
        pres_role="strength", pres={"sets": 3, "reps": 6, "rest_seconds": 30, "tempo": "static"},
        rep_secs=6.0,
    ),

    dict(
        id="kids-ex-0040", slug="single-leg-squat-touch", name="Single Leg Squat Touch",
        desc="A single-leg squat drill where tweens balance on one leg, lower down, and touch the opposite hand to the same-side foot — developing unilateral leg strength, proprioception, and hip stability.",
        focus="Strength", pm=["quads","glutes"], sm=["hamstrings","core"], st=["calves","ankles"],
        sub=["vastus medialis","gluteus medius","tibialis anterior"], mp="squat", family="single-leg-squats",
        dr=3, roles=["main"], bands=TWEENS_ONLY, mt="strength", diff="intermediate", struct="main",
        goals=["build_legs","improve_balance","improve_coordination","home_workout"],
        tags=["intermediate","unilateral","balance","single_leg","lower_body"],
        form=[
            "Stand on your right foot with your left foot slightly lifted.",
            "Slowly bend your right knee and lower your body — like a slow single-leg squat.",
            "As you descend, reach your left hand down toward your right foot.",
            "Touch the foot or just aim close, then drive back up to standing.",
            "Complete all reps on the right before switching to the left."
        ],
        tips=["Keep your knee tracking over your second toe as you lower.",
              "Control the descent — the slower, the harder the exercise."],
        mistakes=["Knee collapsing inward on the descent — actively push the knee out.",
                  "Leaning too far forward — try to keep the torso more upright."],
        wt=45, met=4.5, dur=1.0,
        energy_sys="glycolytic", chain="closed", plane=["sagittal","transverse"], ct=["concentric","eccentric"], ci="compound",
        cns="medium", noise="quiet", space="low", stab="high",
        per_side=True, uni=True,
        pres_role="strength", pres={"sets": 3, "reps": 6, "rest_seconds": 40, "tempo": "slow"},
        rep_secs=4.0,
    ),

    dict(
        id="kids-ex-0041", slug="quadruped-hip-extension-kids", name="Quadruped Hip Extension",
        desc="A glute isolation exercise where tweens start on all fours and extend one leg straight back and up — building gluteus maximus activation and core stability through a simple, safe pattern.",
        focus="Strength", pm=["glutes"], sm=["hamstrings","core","back"], st=["shoulders","wrists"],
        sub=["gluteus maximus","erector spinae","multifidus"], mp="hip_extension", family="glute-activation",
        dr=1, roles=["warmup","main"], bands=TWEENS_ONLY, mt="strength", diff="beginner", struct="main",
        goals=["build_glutes","build_core","improve_posture","home_workout"],
        tags=["low_impact","beginner_friendly","glutes","core","no_equipment","glute_activation"],
        form=[
            "Start on hands and knees — wrists under shoulders, knees under hips.",
            "Keep your back flat — it should look like a table-top.",
            "Extend your right leg straight back, keeping the foot flexed (toes pointing down).",
            "Lift the right leg until it is parallel to the floor — no higher.",
            "Hold for 2 seconds, squeezing the glute, then lower slowly.",
            "Complete all reps on one side before switching."
        ],
        tips=["Don't let your lower back arch when lifting the leg — keep the core braced.",
              "Think of your back as a table you can't spill a glass of water from."],
        mistakes=["Rotating the hip outward as you lift — keep the leg straight and hips square.",
                  "Lifting the leg too high — this causes the lower back to arch."],
        wt=45, met=3.0, dur=1.0,
        energy_sys="phosphagen", chain="open", plane=["sagittal"], ct=["concentric","eccentric","isometric"], ci="isolation",
        cns="low", noise="quiet", space="low", stab="medium",
        per_side=True, uni=True,
        pres_role="strength", pres={"sets": 3, "reps": 12, "rest_seconds": 20, "tempo": "controlled"},
        rep_secs=3.0,
    ),

    dict(
        id="kids-ex-0042", slug="box-step-up-bodyweight", name="Box Step-Up",
        desc="A unilateral lower body strength drill where tweens step onto a raised surface and fully extend the hip at the top — training single-leg quad and glute strength, balance, and knee stability.",
        focus="Strength", pm=["quads","glutes"], sm=["hamstrings","calves"], st=["core","ankles"],
        sub=["vastus lateralis","gluteus maximus"], mp="squat", family="step-up-variations",
        dr=2, roles=["main"], bands=TWEENS_ONLY, mt="strength", diff="beginner", struct="main",
        goals=["build_legs","improve_balance","improve_coordination","home_workout"],
        tags=["low_impact","beginner_friendly","unilateral","lower_body","step_up"],
        form=[
            "Stand facing a stable step, box, or stair (20–30 cm high).",
            "Place your right foot fully on the step.",
            "Drive through your right heel to step up — bring your left foot up beside it.",
            "Stand tall at the top, then step back down with the left foot first.",
            "Complete all reps on the right before switching to lead with the left foot."
        ],
        tips=["Drive through the heel of the stepping foot — not your toes.",
              "Avoid pushing off the floor with the trailing leg — let the step-up leg do the work."],
        mistakes=["Leaning forward excessively — try to stay upright as you step up.",
                  "Using the back leg to push — the drill is single-leg, so the trailing foot is just a passenger."],
        wt=45, met=5.0, dur=1.0,
        energy_sys="glycolytic", chain="closed", plane=["sagittal"], ct=["concentric","eccentric"], ci="compound",
        cns="medium", noise="quiet", space="medium", stab="medium",
        per_side=True, uni=True,
        pres_role="strength", pres={"sets": 3, "reps": 8, "rest_seconds": 30, "tempo": "controlled"},
        rep_secs=3.0,
    ),

    dict(
        id="kids-ex-0043", slug="hip-hinge-introduction", name="Hip Hinge Introduction",
        desc="A fundamental movement pattern drill where tweens learn to hinge at the hips while maintaining a neutral spine — the foundational movement behind jumping, running, lifting, and most athletic activities.",
        focus="Flexibility", pm=["hamstrings","glutes"], sm=["back","core"], st=["calves"],
        sub=["erector spinae","biceps femoris","gluteus maximus"], mp="mobility", family="hip-hinge",
        dr=1, roles=["warmup","main"], bands=TWEENS_ONLY, mt="mobility", diff="beginner", struct="warmup",
        goals=["improve_mobility","improve_flexibility","improve_posture","home_workout"],
        tags=["low_impact","beginner_friendly","movement_pattern","hip_hinge","foundational"],
        form=[
            "Stand with feet hip-width apart and a slight knee bend.",
            "Place your hands on your hips or hold a stick along your spine.",
            "Push your hips back behind you — as if trying to touch the wall behind you.",
            "Your chest moves forward and down while keeping a flat, neutral spine.",
            "Feel the stretch in the back of your legs. Then drive your hips forward to return to standing.",
            "Practice 10 slow, deliberate reps."
        ],
        tips=["Think 'hips back', not 'bend forward' — the hip moves back first.",
              "If you have a wall behind you, try to touch your hips to it on each rep."],
        mistakes=["Rounding the lower back — keep the spine neutral throughout.",
                  "Bending the knees too much — this becomes a squat, not a hinge."],
        wt=45, met=2.5, dur=0.8,
        energy_sys="phosphagen", chain="closed", plane=["sagittal"], ct=["eccentric","concentric"], ci="compound",
        cns="low", noise="quiet", space="low", stab="medium",
        pres_role="mobility", pres={"sets": 3, "reps": 10, "rest_seconds": 30, "tempo": "slow"},
        rep_secs=3.0,
    ),

    dict(
        id="kids-ex-0044", slug="reverse-lunge-walk-kids", name="Reverse Lunge Walk",
        desc="A continuous reverse lunge exercise where tweens step backward into a lunge and alternate legs as they travel forward — building unilateral quad and glute strength with reduced knee-stress compared to forward lunges.",
        focus="Strength", pm=["quads","glutes"], sm=["hamstrings","calves","core"], st=["ankles"],
        sub=["vastus lateralis","gluteus maximus","rectus femoris"], mp="squat", family="lunge-variations",
        dr=2, roles=["main"], bands=TWEENS_ONLY, mt="strength", diff="beginner", struct="main",
        goals=["build_legs","improve_balance","improve_coordination","home_workout"],
        tags=["low_impact","beginner_friendly","unilateral","lower_body","no_equipment"],
        form=[
            "Stand tall with feet hip-width apart and hands at your sides.",
            "Step your right foot backward, lowering your right knee toward the floor.",
            "Front knee (left) should be above the ankle, back knee just off the floor.",
            "Push off the right foot to step forward and stand.",
            "Immediately step the left foot back for the next rep.",
            "Continue alternating as you walk forward across the room."
        ],
        tips=["Keep your torso upright and core braced — don't lean forward.",
              "Lower slow — control is more important than speed in this drill."],
        mistakes=["Front knee going past the toes — keep the shin nearly vertical.",
                  "Back knee banging the floor — lower softly and with control."],
        wt=45, met=4.5, dur=1.0,
        energy_sys="glycolytic", chain="closed", plane=["sagittal"], ct=["concentric","eccentric"], ci="compound",
        cns="low", noise="quiet", space="medium", stab="medium",
        per_side=True, uni=True,
        pres_role="strength", pres={"sets": 3, "reps": 10, "rest_seconds": 30, "tempo": "controlled"},
        rep_secs=3.0,
    ),

    dict(
        id="kids-ex-0045", slug="agility-dot-drill", name="Agility Dot Drill",
        desc="A five-point footwork drill where tweens move rapidly around an imaginary or chalked dot pattern in sequence — developing foot speed, coordination, and change-of-direction quickness.",
        focus="Coordination", pm=["calves","quads"], sm=["glutes","core"], st=["ankles"],
        sub=["gastrocnemius","tibialis anterior","peroneus longus"], mp="locomotion", family="agility-drills",
        dr=2, roles=["warmup","main"], bands=TWEENS_ONLY, mt="cardio", diff="beginner", struct="main",
        goals=["improve_coordination","improve_agility","home_workout","improve_cardio"],
        tags=["low_impact","beginner_friendly","agility","footwork","coordination","speed"],
        tax_sports=["basketball", "soccer", "football", "tennis"],
        form=[
            "Mark or imagine a cross of 5 dots: centre, front-left, front-right, back-left, back-right.",
            "Start in the centre dot and hop to front-left, then front-right.",
            "Hop back to centre, then to back-left, then back-right.",
            "Return to centre — that is one cycle. Complete 5 cycles fast!",
            "Try for 2-footed hops first, then progress to single-leg hops."
        ],
        tips=["Stay on the balls of your feet — flat-footed movement is slower.",
              "Try to memorise the pattern so you don't slow down to think."],
        mistakes=["Landing heavy — stay light and springy.",
                  "Looking at your feet — try to keep your head up."],
        wt=45, met=7.0, dur=0.7,
        energy_sys="glycolytic", chain="closed", plane=["sagittal","frontal"], ct=["concentric","eccentric"], ci="compound",
        cns="high", noise="moderate", space="low", stab="medium",
        pres_role="cardio", pres={"sets": 4, "reps": 5, "rest_seconds": 30},
        rep_secs=3.0,
    ),

    dict(
        id="kids-ex-0046", slug="two-foot-jump-freeze", name="Two-Foot Jump Freeze",
        desc="A plyometric landing drill where tweens perform a two-footed jump then stick the landing absolutely still — teaching controlled deceleration and safe landing mechanics before progressing to more intense jumping exercises.",
        focus="Power", pm=["quads","glutes","calves"], sm=["core","hamstrings"], st=["ankles"],
        sub=["gastrocnemius","gluteus maximus","tibialis anterior"], mp="plyometric", family="jumping-games",
        dr=2, roles=["main"], bands=TWEENS_ONLY, mt="cardio", diff="beginner", struct="main",
        goals=["improve_power","improve_balance","improve_coordination","home_workout"],
        tags=["low_impact","beginner_friendly","plyometric","landing_mechanics","sport_prep"],
        form=[
            "Stand with feet hip-width apart in a slight crouch.",
            "Jump up (or forward), getting good height or distance.",
            "As you land, bend your knees to absorb and FREEZE — don't take a step.",
            "Hold the landing position for 3 seconds: knees bent, arms forward, eyes ahead.",
            "Check yourself: are your knees tracking over your toes? Is your chest up?",
            "Stand, reset, and repeat."
        ],
        tips=["Aim for silent landing — the quieter, the better your cushioning technique.",
              "Pause after every jump to evaluate your landing position before the next rep."],
        mistakes=["Jumping too high before mastering the landing — progress gradually.",
                  "Knees caving inward on landing — push them out actively."],
        wt=45, met=6.0, dur=0.8,
        energy_sys="phosphagen", chain="closed", plane=["sagittal"], ct=["concentric","eccentric"], ci="compound",
        cns="medium", noise="moderate", space="medium", stab="high",
        pres_role="strength", pres={"sets": 3, "reps": 8, "rest_seconds": 30, "tempo": "controlled"},
        rep_secs=4.0,
    ),

    dict(
        id="kids-ex-0047", slug="side-plank-modified-kids", name="Side Plank Modified",
        desc="A beginner lateral core stability hold where tweens support their body from their forearm and knee (rather than feet) in a side plank — building oblique strength and lateral trunk stability progressively.",
        focus="Strength", pm=["core"], sm=["shoulders","glutes","back"], st=["wrists"],
        sub=["obliques","quadratus lumborum","gluteus medius"], mp="hold", family="plank-variations",
        dr=2, roles=["main"], bands=TWEENS_ONLY, mt="strength", diff="beginner", struct="main",
        goals=["build_core","improve_posture","home_workout"],
        tags=["low_impact","beginner_friendly","core","lateral","no_equipment"],
        form=[
            "Lie on your right side with your right forearm flat on the floor, elbow under shoulder.",
            "Stack your left knee on top of the right knee — this is the modified position.",
            "Lift your hips off the floor — your body should form a straight line from head to knees.",
            "Hold for 10–30 seconds, keeping hips from sagging or rotating.",
            "Lower, rest, and repeat on the left side."
        ],
        tips=["Press the floor away with your forearm to keep the shoulder strong.",
              "Stack your hips — make sure the top hip doesn't rotate back."],
        mistakes=["Hips sagging toward the floor — keep them lifted.",
                  "Shoulder collapsing — actively press the floor and elevate the torso."],
        wt=45, met=3.0, dur=0.8,
        energy_sys="phosphagen", chain="closed", plane=["frontal"], ct=["isometric"], ci="compound",
        cns="low", noise="quiet", space="low", stab="medium",
        per_side=True,
        is_hold=True, hold_secs=20,
        pres_role="strength", pres={"sets": 3, "duration_seconds": 20, "rest_seconds": 30, "tempo": "static"},
        rep_secs=20.0,
    ),

    dict(
        id="kids-ex-0048", slug="lateral-band-walk-no-band", name="Lateral Band Walk (No Band)",
        desc="A lateral stepping drill performed with deliberate hip abductor muscle activation without equipment — mimicking the resistance band version to train gluteus medius, hip stability, and knee tracking with bodyweight only.",
        focus="Strength", pm=["glutes"], sm=["quads","core"], st=["ankles"],
        sub=["gluteus medius","tensor fasciae latae","hip abductors"], mp="locomotion", family="lateral-movement",
        dr=1, roles=["warmup","main"], bands=TWEENS_ONLY, mt="strength", diff="beginner", struct="warmup",
        goals=["build_glutes","improve_balance","improve_posture","home_workout"],
        tags=["low_impact","beginner_friendly","glute_activation","hip_stability","warmup"],
        tax_sports=["basketball", "soccer", "football", "tennis"],
        form=[
            "Stand with feet hip-width apart and a slight squat (athletic position).",
            "Step your right foot out to the right — about shoulder-width away from the left.",
            "Follow with the left foot so you return to hip-width stance.",
            "Take 8 steps to the right, then 8 steps back to the left.",
            "Focus on actively squeezing your outer hip on every step — don't just shuffle."
        ],
        tips=["Keep the knees slightly bent throughout — don't stand up between steps.",
              "Actively push your knees out as you step — this is the whole point of the drill."],
        mistakes=["Letting the knees cave inward — actively push them out.",
                  "Standing up fully between steps — maintain the athletic stance."],
        wt=45, met=3.5, dur=1.0,
        energy_sys="phosphagen", chain="closed", plane=["frontal"], ct=["concentric","isometric"], ci="isolation",
        cns="low", noise="quiet", space="medium", stab="medium",
        pres_role="strength", pres={"sets": 3, "reps": 8, "rest_seconds": 30, "tempo": "controlled"},
        rep_secs=1.5,
    ),

    dict(
        id="kids-ex-0049", slug="coordination-ladder-drill", name="Coordination Ladder Drill",
        desc="A footwork-pattern drill performed over an imaginary or drawn ladder on the floor — teaching foot placement precision, rhythm, and multi-directional agility without any equipment.",
        focus="Coordination", pm=["calves","quads"], sm=["core","glutes","hip_flexors"], st=["ankles"],
        sub=["gastrocnemius","tibialis anterior","hip flexors"], mp="locomotion", family="agility-drills",
        dr=2, roles=["warmup","main"], bands=TWEENS_ONLY, mt="cardio", diff="beginner", struct="warmup",
        goals=["improve_coordination","improve_agility","improve_cardio","home_workout"],
        tags=["low_impact","beginner_friendly","agility","footwork","coordination","speed"],
        tax_sports=["basketball", "soccer", "football", "tennis", "baseball"],
        form=[
            "Draw or imagine 8–10 squares in a line on the floor (each about 45 cm wide).",
            "Pattern 1 (In-In-Out-Out): Step both feet into the first square, step both feet out to the sides, move forward to the next square.",
            "Pattern 2 (Two-Foot Hop): Two-foot hop into every square.",
            "Pattern 3 (Single Leg): Hop on your right foot through all squares, then left.",
            "Walk back to the start and try the next pattern.",
            "Start slow to build accuracy, then increase speed."
        ],
        tips=["Accuracy before speed — nail the pattern at 50% speed first.",
              "Pump your arms to stay in rhythm — arms and legs work together."],
        mistakes=["Going flat-footed — stay on your toes throughout.",
                  "Skipping squares — precision matters as much as speed."],
        wt=45, met=6.5, dur=1.0,
        energy_sys="glycolytic", chain="closed", plane=["sagittal","frontal"], ct=["concentric","eccentric"], ci="compound",
        cns="high", noise="moderate", space="medium", stab="medium",
        pres_role="cardio", pres={"sets": 4, "reps": 3, "rest_seconds": 30},
        rep_secs=5.0,
    ),

    dict(
        id="kids-ex-0050", slug="dynamic-forward-plank-shift", name="Dynamic Forward Plank Shift",
        desc="A dynamic core anti-extension exercise where tweens shift their high-plank body forward and back over their hands — increasing the lever arm and challenging deep abdominal and shoulder stability beyond a static plank.",
        focus="Strength", pm=["core","shoulders"], sm=["chest","back","glutes"], st=["wrists"],
        sub=["rectus abdominis","transversus abdominis","anterior deltoid","serratus anterior"], mp="anti_extension", family="plank-variations",
        dr=3, roles=["main"], bands=TWEENS_ONLY, mt="strength", diff="intermediate", struct="main",
        goals=["build_core","build_upper_body","improve_posture","home_workout"],
        tags=["intermediate","core","no_equipment","shoulder_stability","anti_extension"],
        form=[
            "Start in a high plank with hands under shoulders, body straight.",
            "Keeping your whole body rigid (don't bend at the hips), slowly shift your shoulders forward over your hands.",
            "Move about 5–10 cm forward, then shift back to the start position.",
            "The movement is small and controlled — think of shifting like a human lever.",
            "Complete 8–10 slow shifts."
        ],
        tips=["Brace your core as hard as possible before you start moving.",
              "Keep the shift slow — 2 seconds forward, 2 seconds back is ideal."],
        mistakes=["Sagging the hips as you shift forward — keep the body like a board.",
                  "Bending the elbows — this should be a shoulder shift, not an elbow push-up."],
        wt=45, met=4.0, dur=1.0,
        energy_sys="phosphagen", chain="closed", plane=["sagittal"], ct=["isometric","concentric"], ci="compound",
        cns="medium", noise="quiet", space="low", stab="low",
        pres_role="strength", pres={"sets": 3, "reps": 10, "rest_seconds": 40, "tempo": "slow"},
        rep_secs=4.0,
    ),
]

# ── PART B: SPORTS MAPPING ─────────────────────────────────────────────────────

SPORTS_UPDATES = {
    "Band Front Raises":              ["boxing", "tennis"],
    "Band Front Raises, Palms Up":    ["boxing", "tennis"],
    "Band Shoulder Dislocations":     ["baseball", "tennis", "boxing"],
    "Band Tricep Extensions":         ["boxing", "tennis", "baseball"],
    "Body Saws":                      ["soccer", "basketball", "football"],
    "Bridge":                         ["football", "running"],
    "Cat-Cow Stretch":                ["golf"],
    "Chest Stretch":                  ["boxing", "baseball", "tennis"],
    "Cobra Pose":                     ["running"],
    "Dancer Pose":                    ["running"],
    "Deep Squat":                     ["basketball", "football", "baseball"],
    "Donkey Bent Knee Kicks":         ["running", "soccer"],
    "Downward Facing Dog":            ["running"],
    "Dumbbell Get-Ups":               ["boxing", "football"],
    "Dumbbell Lateral Raise Circles": ["tennis", "baseball"],
    "Dumbbell Lateral Raises":        ["tennis", "baseball"],
    "Dumbbell Overhead Tricep Extensions": ["basketball", "tennis", "baseball"],
    "Dumbbell Press with 3s Iso-Hold": ["boxing", "basketball"],
    "Dumbbell Rear Delt Raises":      ["baseball", "tennis"],
    "Dumbbell Side Bend":             ["golf", "tennis"],
    "Flutter Kicks":                  ["soccer"],
    "Glute Foam Roll":                ["running", "basketball"],
    "Hamstring Foam Roll":            ["running", "soccer", "football", "basketball"],
    "Hamstring Stretch":              ["running", "soccer", "football", "basketball", "tennis"],
    "Head-to-Knee":                   ["running"],
    "Isometric Dumbbell Lateral Raises": ["tennis", "baseball"],
    "Kneeling to Stand-Up":           ["football", "basketball"],
    "Lat Foam Roll":                  ["baseball", "tennis", "basketball"],
    "Lateral Raise Circles":          ["tennis", "baseball"],
    "Lateral Shoulder Stretch":       ["baseball", "tennis", "boxing"],
    "Locust Pose":                    ["running"],
    "Puppy Stretch":                  ["basketball", "tennis", "baseball"],
    "Pyramid Pose":                   ["running", "soccer"],
    "Reverse Snow Angel":             ["baseball", "tennis"],
    "Reverse Snow Angels":            ["baseball", "tennis", "boxing"],
    "Revolved Side Angle":            ["golf", "tennis"],
    "Scapula Slides":                 ["baseball", "tennis", "boxing"],
    "Scissors":                       ["soccer", "football"],
    "Seated Cat-Cow Stretch":         ["golf"],
    "Seated Side Stretch":            ["golf", "tennis"],
    "Shoulder Circles":               ["baseball", "tennis", "boxing"],
    "Sit-and-Reach":                  ["running", "soccer"],
    "Sphinx Pose":                    ["running"],
    "Standing Backbend":              ["golf"],
    "Standing Cat-Cow Stretch":       ["golf"],
    "Standing Lateral Shoulder Stretch": ["baseball", "tennis", "boxing"],
    "Standing Roll Down and Up":      ["golf", "running"],
    "Stepper":                        ["running", "basketball"],
    "Straddle Pose":                  ["soccer"],
    "Straddle Side Bend":             ["soccer"],
    "Superman":                       ["running", "football"],
    "Swiss Ball Hamstring Curls":     ["running", "soccer", "football"],
    "Swiss Ball Reverse Extensions":  ["running", "football"],
    "Triceps Stretch":                ["baseball", "tennis", "boxing"],
    "Twisted Chair Pose":             ["golf", "tennis"],
    "Upper Back Foam Roll":           ["running", "baseball", "tennis"],
    "Wide-Legged Side Stretch":       ["soccer", "basketball"],
}

# ── MAIN ───────────────────────────────────────────────────────────────────────

def main():
    with open(SRC) as f:
        data = json.load(f)

    original_count = len(data)

    # Part A: add new exercises
    new_exercises = [build_ex(d) for d in DEFS]
    data.extend(new_exercises)
    print(f"Part A: added {len(new_exercises)} new exercises (total now {len(data)})")

    # Part B: update sports_suggested for exercises with empty list
    updated = 0
    for ex in data:
        name = ex.get('name', '')
        if name in SPORTS_UPDATES:
            tax = ex.get('taxonomy', {})
            if tax.get('sports_suggested') == []:
                tax['sports_suggested'] = SPORTS_UPDATES[name]
                updated += 1

    print(f"Part B: updated sports_suggested on {updated} exercises")

    with open(SRC, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Saved to {SRC}")

    # ── SUMMARY ───────────────────────────────────────────────────────────────
    all_exs = data

    # Count by age_bands_suggested
    from collections import Counter, defaultdict
    band_counts = Counter()
    for ex in all_exs:
        bands = ex.get('taxonomy', {}).get('age_bands_suggested', [])
        for b in bands:
            band_counts[b] += 1
    # also count exercises with no band
    no_band = sum(1 for ex in all_exs if not ex.get('taxonomy', {}).get('age_bands_suggested'))
    print("\n── Age Band Distribution (taxonomy.age_bands_suggested) ──")
    for band, count in sorted(band_counts.items()):
        print(f"  {band}: {count}")
    print(f"  (no band / general): {no_band}")

    # Count by sports_suggested
    sport_counts = Counter()
    for ex in all_exs:
        sports = ex.get('taxonomy', {}).get('sports_suggested', [])
        for s in sports:
            sport_counts[s] += 1
    empty_sport = sum(1 for ex in all_exs if not ex.get('taxonomy', {}).get('sports_suggested'))
    print("\n── Sport Distribution (taxonomy.sports_suggested) ──")
    for sport, count in sorted(sport_counts.items(), key=lambda x: -x[1]):
        print(f"  {sport}: {count}")
    print(f"  (no sport tag): {empty_sport}")

    # Count by movement_type (taxonomy)
    mt_counts = Counter()
    for ex in all_exs:
        mt = ex.get('taxonomy', {}).get('movement_type')
        if mt:
            mt_counts[mt] += 1
    print("\n── Movement Type Distribution (taxonomy.movement_type) ──")
    for mt, count in sorted(mt_counts.items(), key=lambda x: -x[1]):
        print(f"  {mt}: {count}")


if __name__ == '__main__':
    main()
