
def check_signal_state_transition(signal: list[int], expected: list[int]) -> bool:
    """
    Check if the signal states of the given signal arrive in the expected order.

    Check if the input 'signal' contains exactly one occurrence of the expected state progression provided in the 'expected' list.
    Time Complexity: O(n)
    Space Complexity: O(1)

    Example: for signal [1,1,1,2,2,3] and expected [1,2,3], the function will return True.
    Example2: for signal [1,2,2] and expected [1,2,3], the function will return False.
    """
    if not signal or not expected:
        return False

    current_index = 0  # Index to track position in expected list
    found_complete_sequence = False

    for value in signal:
        if value == expected[current_index]:
            if current_index == len(expected) - 1:
                if found_complete_sequence:
                    return False  # Found a second sequence, this is not allowed
                found_complete_sequence = True
                current_index = 0  # Reset to look for potential repeated sequence
            elif value != expected[current_index + 1]:
                current_index += 1

    return found_complete_sequence
