# Experimenting with Communicating between Threads with Queues

A simplistic load balancer.

Has a receiver that distributes messages to workers via a naive round robin approach. Messages are added to worker input queues for processing.

Workers read from their input queue, do work (in this case, a number of rounds of hashing) and deliver their results to their output queues.

Sender threads read from output queues and do the actual sending.