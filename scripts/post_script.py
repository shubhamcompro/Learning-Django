from posts.models import Post, Tag
from django.contrib.auth.models import User
import random

# from scripts import post_script
# post_script.run()

def run():
	users = User.objects.all()
	usersSize = len(users)
	tags = Tag.objects.all()
	tagsSize = len(tags)

	posts = Post.objects.all()
	for post in posts:
		post.delete()

	for i in range(0, 200):
		user = users[random.randint(0, usersSize - 1)]
		tag1 = tags[random.randint(0, tagsSize - 1)]
		tag2 = tags[random.randint(0, tagsSize - 1)]

		while tag1.name == tag2.name:
			tag2 = tags[random.randint(0, tagsSize - 1)]

		for j in range(10000000):
			pass

		post = Post(title=f'this is {i}th post by {user.username}', description='Sample description', user=user,
					active=(random.randint(0, 1) == 1))
		print('created ', i, 'post')
		post.save()
		post.tags.add(tag1)
		post.tags.add(tag2)
		post.save()


if __name__ == '__main__':
	run()
