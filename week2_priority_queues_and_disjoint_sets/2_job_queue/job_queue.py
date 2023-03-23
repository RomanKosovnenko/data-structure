# python3
import heapq
from collections import namedtuple

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return not self.elements

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    workers_queue = PriorityQueue()
    for i in range(n_workers):
        workers_queue.put(i, 0)
    for job in jobs:
        next_worker = workers_queue.get()
        result.append(AssignedJob(next_worker[1], next_worker[0]))
        workers_queue.put(next_worker[1], next_worker[0]+job)

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
