import cognitive_face as CF

class Faces:

    def __init__(self, key):
        self.KEY = key
        CF.Key.set(key)

    def new_pic(self, img_url):
        self.img_url = img_url

    def add_group(self, group_id):
        group_id = CF.person_group.create(group_id)
        return group_id

    def add_person(self, group_id, name):
        person_id = CF.person.create(group_id, name)
        return person_id['personId']

    def add_person_face(self, group_id, person_id):
        persisted_face_id = CF.person.add_face(self.img_url, group_id, person_id)
        return persisted_face_id

    def train_group(self, group_id):
        CF.person_group.train(group_id)

    def get_best_candidate(self, info, face_id, group_id):
        """ info is a list of dictionaries, like so:
            [{'faceId': '1', 'candidates': [{'personId': '6', 'confidence': 0.63223}]}]
            
            Returns the candidate with the most confidence
        """
        max_confidence = -1
        candidates = {}
        for faces in info:
            if faces['faceId'] == face_id:
                for candidate in faces['candidates']:
                    candidates[candidate['confidence']] = candidate['personId']
                    max_confidence = max(max_confidence, candidate['confidence'])

        best_candidate_id = candidates[max_confidence]
        best_candidate_name = CF.person.get(group_id, best_candidate_id)['name']

        return best_candidate_name



    def add_pic_person_face(self):
        group_choice = input("Is the person a celebrity or not? ('Y' or 'N') \n")
        if (group_choice == 'Y' or group_choice == 'y'):
            group_id = 'celeb'
        else:
            group_id = 'normal'


        person_name = input("What is your person's name? \n")
        person_id = self.add_person(group_id, person_name)
        self.add_person_face(group_id, person_id)
        print("Finished adding :)\n")

    def identify(self):
        group_choice = input("Is the person a celebrity or not? ('Y' or 'N') \n")
        if (group_choice == 'Y' or group_choice == 'y'):
            group_id = 'celeb'
        else:
            group_id = 'normal'

        # Train the group before identification

        CF.person_group.train(group_id)
        print("We are training the group right now for identification, may take a while (usually fast).\n"
              "If you get an error message with regards to training, please wait and try again later :)\n")
        print("Here is the training status for this group: \n")
        print(CF.person_group.get_status(group_id)['status'])

        # Need to generate the list of faces for the input of detect, maximum 10 in the uploaded picture
        list_of_faces = []
        detection_info = CF.face.detect(self.img_url)
        for item in detection_info:
            list_of_faces.append(item['faceId'])

        # Start detection
        identification_result = CF.face.identify(list_of_faces, group_id)
        print("Identification finished, here are the results: \n")
        for face in list_of_faces:
            print(self.get_best_candidate(identification_result, face, group_id))



if __name__ == "__main__":
    isDone = False
    key = input("Please enter your Microsoft subscription key: \n")
    sim = Faces(key)
    while isDone == False:
        image = input("Please input the URL of the image of the person you want to add or identify: \n")
        sim.new_pic(image)
        add_identify = input("Would you like to add a person or identify a person? ('A' for add, 'I' for identify) \n")
        if (add_identify) == 'A':
            sim.add_pic_person_face()
        elif (add_identify == 'I'):
            sim.identify()
        end = input("Would you like to do end this session? ('Y' or 'N') \n")
        if (end != 'n' and end != 'N'):
            isDone = True






















