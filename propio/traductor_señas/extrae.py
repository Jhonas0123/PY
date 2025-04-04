landmark_list = []
if result.multi_hand_landmarks:
    for hand_landmarks in result.multi_hand_landmarks:
        for lm in hand_landmarks.landmark:
            landmark_list.append([lm.x, lm.y, lm.z])
