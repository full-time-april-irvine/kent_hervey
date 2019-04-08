class SLNode:
 def __init__(self, value):
  self.value = value
  self.next = None



class SList:
    def __init__(self):
    	self.head = None

    def add_to_front(self, val):	
        new_node = SLNode(val)	# create a new instance of our Node class using the given value
        current_head = self.head	# save the current head in a variable
        new_node.next = current_head	# SET the new node's next To the list's current head
        #new_node.next is now storing the memory location that current_head is storing, and will continue to store
        self.head = new_node	# SET the list's head TO the node we created in the last step
        #self.head is a property...We are overriding it with the memeory location stored in new_node
        return self	                # return self to allow for chaining
    #Traversing Through a List
    def print_values(self):
        runner = self.head	        # a pointer to the list's first node
        #self.head was and is a reference to a memory location storing the head value
        while (runner != None):	    # iterating while runner is a node and not None
            print(runner.value)     #print the current node's value
            runner = runner.next    #set the runner to its neighbor
            #except for the last node, reference is being stored.  NONE is a primitive type, so stored by values.
        return self             #once the loop is done, return self to allow for chaining

    # Traversing Through a List and Adding a Value to the End
    def add_to_back(self, val):
        if self.head == None:       # if the list is empty
            self.add_to_front(val)  #run the add_to_front method
            return self             # le's make sure the rest of this function doesn't happen if we add to the front
        new_node = SLNode(val)      #create a new instance of our Node class with the given value
        runner = self.head          # set an iterator to start at the front of the list
        while (runner.next !=None): #iterate until the iterator does not have a neighbor
            runner = runner.next    
    #   When the loop has finished running, runner will be pointing to the last node. Its next is currently set to None, but we want to make the new node we created at the beginning of this method to be its neighbor:   
        runner.next = new_node      #increment the runner to the next node in the list
        return self
    def print_values_mod(self):
        runner = self.head	        # a pointer to the list's first node
        while (runner != None):	    # iterating while runner is a node and not None
            print("current node's value is:  " , runner.value)     #print the current node's value , self.head.value
            runner = runner.next    #set the runner to its neighbor
        return self             #once the loop is done, return self to allow for chaining




#Let's test our function
my_list = SList()       # create a new instance of a list
#my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values_mod()

my_list.add_to_front("this should be first")


my_list.add_to_back("2")
my_list.add_to_back("3")
my_list.add_to_back("4")
my_list.print_values_mod()




#output should be
#Linked lists
# are
# fun!







print("me"*55)