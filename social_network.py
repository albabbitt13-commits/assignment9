class Person:
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        # Prevent duplicate friendships
        if friend not in self.friends:
            self.friends.append(friend)


class SocialNetwork:
    def __init__(self):
        # Adjacency list representation
        self.people = {}

    def add_person(self, name):
        if name in self.people:
            print(f"{name} already exists in the network.")
        else:
            self.people[name] = Person(name)

    def add_friendship(self, person1_name, person2_name):
        if person1_name not in self.people:
            print(f"Friendship not created. {person1_name} doesn't exist!")
            return

        if person2_name not in self.people:
            print(f"Friendship not created. {person2_name} doesn't exist!")
            return

        person1 = self.people[person1_name]
        person2 = self.people[person2_name]

        # Bidirectional friendship
        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):
        for person in self.people.values():
            friend_names = [friend.name for friend in person.friends]
            print(f"{person.name} is friends with: {', '.join(friend_names)}")


# Testing

network = SocialNetwork()

# Add people
network.add_person("Alex")
network.add_person("Jordan")
network.add_person("Morgan")
network.add_person("Taylor")
network.add_person("Casey")
network.add_person("Riley")

# Test duplicate
network.add_person("Alex")

# Create friendships
network.add_friendship("Alex", "Jordan")
network.add_friendship("Alex", "Morgan")
network.add_friendship("Jordan", "Taylor")
network.add_friendship("Morgan", "Casey")
network.add_friendship("Taylor", "Riley")
network.add_friendship("Casey", "Riley")
network.add_friendship("Morgan", "Riley")
network.add_friendship("Alex", "Taylor")

# Test missing person
