import cognitive_face as CF

KEY = '043cb9a6ac2941b5a9d92801f0f6629d'  # Replace with a valid subscription key (keeping the quotes in place).
CF.Key.set(KEY)

# You can use this example JPG or replace the URL below with your own URL to a JPEG image.
# img_url = 'http://static1.businessinsider.com/image/55cdf76f371d2215008bfddf-1500/mark%20zuckerberg-6.jpg'
img_url2 = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1496051584&di=3d079dc32a276aef5dbc20f50c01a876&imgtype=jpg&er=1&src=http%3A%2F%2Fguyanachronicle.com%2Fwp-content%2Fuploads%2F2014%2F02%2FFacebook-Owner.jpg'

#img_url = input("Please enter url of the picture: \n")

""" CF.person_group.create("madting", "celebs")
mark_id = CF.person.create("madting", "mark")
print(mark_id)
faceId = CF.person.add_face(img_url, "madting", mark_id['personId'])
print("\n")
print(faceId)

identify_info = CF.face.detect(img_url2)
print(identify_info)
list1 = []
list1.append(identify_info[0]['faceId'])
identify_result = CF.face.identify(list1, "madting", 1)

group_id = "madting"
list_of_faces = []
detection_info = CF.face.detect(img_url2)
for item in detection_info:
    list_of_faces.append(item['faceId'])

# Start detection
result = CF.face.identify(list_of_faces, group_id)


print(max(result[0]['candidates'][0]['confidence'], 0))

"""
list_of_faces = []
detection_info = CF.face.detect(img_url2)
for item in detection_info:
    list_of_faces.append(item['faceId'])
print(list_of_faces)