
import time
from multiprocessing import Process, Queue, cpu_count
from . import MonteCarlo


def mc_thread(self, q, function):

    q.put(function().mean)


class ThreadedMonteCarlo:

    def __init__(self, value_function, n, **kwargs):

        start_time = time.time()

        self.queue = Queue()
        self.processes = []
        self.n_cpu = cpu_count()

        for i in range(cpu_count()):

            self.processes.append(
                Process(
                    target=lambda q: q.put(
                        MonteCarlo(
                            value_function,
                            n / self.n_cpu,
                            skip=i * (n / self.n_cpu),
                            **kwargs).mean),
                    args=(self.queue,)))

        for process in self.processes:
            process.start()

        for process in self.processes:
            process.join()

        total = 0
        while not self.queue.empty():
            total += self.queue.get()
        self.mean = total / self.n_cpu

        self.time = time.time() - start_time
