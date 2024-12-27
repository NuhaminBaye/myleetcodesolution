class RecentCounter:
    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        # Add the new request time
        self.requests.append(t)
        # Calculate the lower bound of the time frame
        lower_bound = t - 3000
        # Filter requests to count only those within the range [lower_bound, t]
        while self.requests[0] < lower_bound:
            self.requests.pop(0)
        # Return the count of requests in the time frame
        return len(self.requests)

# Example usage:
if __name__ == "__main__":
    recentCounter = RecentCounter()