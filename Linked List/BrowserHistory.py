class Node:
    def __init__(self, value):
        # self.key = key
        self.value = value
        self.next = None
        self.prev = None


class BrowserHistory:

    def __init__(self, homepage):
        self.currentPage = Node(homepage)
        
        
    def visit(self, url):
        node = Node(url)
        self.currentPage.next = node
        node.prev = self.currentPage
        self.currentPage = node
        

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """

        while self.currentPage.prev and steps > 0:
            self.currentPage = self.currentPage.prev
            steps -= 1
        
        return self.currentPage.value

        

    def forward(self, steps):
        while self.currentPage.next and steps > 0:
            self.currentPage = self.currentPage.next
            steps -= 1
        
        return self.currentPage.value
        
    def __str__(self):
        
        current = self.currentPage
        result = ""
        while current:
            result += str(current.value) + " => "
            current = current.prev
        
        result = result[:-4]
        # print(self.size)
        print("Current Page :" , self.currentPage.value )
        return result
            
        
        
browserHistory = BrowserHistory("leetcode.com");
browserHistory.visit("google.com");   #// You are in "leetcode.com". Visit "google.com"
browserHistory.visit("facebook.com")  #// You are in "google.com". Visit "facebook.com"
browserHistory.visit("youtube.com");  #// You are in "facebook.com". Visit "youtube.com"
b1 = browserHistory.back(1);               #// You are in "youtube.com", move back to "facebook.com" return "facebook.com"
browserHistory.back(1);               #// You are in "facebook.com", move back to "google.com" return "google.com"
browserHistory.forward(1);            #// You are in "google.com", move forward to "facebook.com" return "facebook.com"
browserHistory.visit("linkedin.com")  #// You are in "facebook.com". Visit "linkedin.com"
browserHistory.forward(2);            #// You are in "linkedin.com", you cannot move forward any steps.
browserHistory.back(2);               #// You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
browserHistory.back(7);               #// You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"