import random


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # Add users
        for name in range(num_users):
            self.add_user(name+1)
        # Create friendships
        full_friendships_list = []
        for name_1 in range(num_users):
            for name_2 in range(name_1+1, num_users):
                full_friendships_list.append((name_1+1, name_2+1))
        # Shuffle relationships
        random.shuffle(full_friendships_list)
        friendships_needed = int(num_users*avg_friendships/2)
        friends_graph = full_friendships_list[:friendships_needed]
        # Add friendship
        for name_1, name_2 in friends_graph:
            self.add_friendship(name_1, name_2)

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # Create an empty queue and enqueue A PATH TO starting vertext ID
        queue = Queue()
        queue.enqueue([user_id])
        # While the que is not empty..
        while queue.size() > 0:
            # Deqeue the first PATH
            path = queue.dequeue()
            # Grab last vertex from the PATH
            vertex = path[-1]
            # If that vertex hasn't been visited..
            if vertex not in visited:
                # Mark it as visited
                visited[vertex] = path
                # Then add A PATH to its neighbors to the back of the queue
                for neighbor in self.friendships[vertex]:
                    # COPY THE PATH
                    new_path = path.copy()
                    # APPEND THE NEIGHBOR TO THE BACK
                    new_path.append(neighbor)
                    queue.enqueue(new_path)

        """Extended social network statistics"""
        # ext_users = len(visited)-1
        # other_users_percent = ext_users/(len(self.users)-1)*100
        # print(f'{other_users_percent:.2f}% of other users in User({user_id}) extended social network')
        # average_degree = sum([len(visited[v_id])-1 for v_id in visited if v_id != user_id])/ext_users
        # print(f'{average_degree:.2f} avg degree of separation between User({user_id}) and those in his/her extended network')

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    # Creates users with an avg friendships each
    num_users = 1000
    avg_friendships = 5
    sg.populate_graph(num_users, avg_friendships)
    print(sg.friendships)
    user_id = 2
    connections = sg.get_all_social_paths(user_id)
    print(connections)
