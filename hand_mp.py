from pprint import pprint
import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# For webcam input:
cap = cv2.VideoCapture(0)


hand_info = {}


def convert_hand_landmarks_to_json(hand_landmarks):
    data = []
    for h in hand_landmarks:
        hand = []
        for l in h.landmark:
            hand.append({"x": l.x, "y": l.y, "z": l.z})
        data.append(hand)
    return data


def start_gettin_handy_info(shared_hand_data):
    global hand_info
    with mp_hands.Hands(
        model_complexity=0, min_detection_confidence=0.5, min_tracking_confidence=0.5
    ) as hands:
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("Ignoring empty camera frame.")
                # If loading a video, use 'break' instead of 'continue'.
                continue

            # To improve performance, optionally mark the image as not writeable to
            # pass by reference.
            image.flags.writeable = False
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = hands.process(image)

            # Draw the hand annotations on the image.
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            if results.multi_hand_landmarks:
                # convert landmarks to json
                j = convert_hand_landmarks_to_json(results.multi_hand_landmarks)
                shared_hand_data.data = j
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        image,
                        hand_landmarks,
                        mp_hands.HAND_CONNECTIONS,
                        mp_drawing_styles.get_default_hand_landmarks_style(),
                        mp_drawing_styles.get_default_hand_connections_style(),
                    )

            # Flip the image horizontally for a selfie-view display.
            cv2.imshow("MediaPipe Hands", cv2.flip(image, 1))
            if cv2.waitKey(5) & 0xFF == 27:
                break
    cap.release()


if __name__ == "__main__":
    start_gettin_handy_info("")
