from googleapiclient.discovery import build
youtube=build('youtube','v3',developerKey='AIzaSyDmeKQ71AAJksvhHbzxycrAaZ6VlfcfQfk')

#search for channel id
#print("Enter name of channel")
#x=input()
#request=youtube.channels().list(part="statistics", forUsername=x)
#response=request.execute()
#print(response)


#search for videos
print("Enter search term")
x=input()
request=youtube.search().list(part="snippet",q=x)
response=request.execute()
print(response['items'][0])
