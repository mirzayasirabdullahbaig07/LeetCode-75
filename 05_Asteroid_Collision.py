class Solution:
    def asteroidCollision(self, asteroids):

        # Size of the array
        n = len(asteroids)

        # List implementation of stack
        st = []

        # Traverse all the asteroids
        for i in range(n):

            # Push the asteroid in stack if a
            # right moving asteroid is seen
            if asteroids[i] > 0:
                st.append(asteroids[i])

            # Else if the asteroid is moving
            # left, perform the collisions
            else:

                # Until the right moving asteroids are
                # smaller in size, keep on destroying them
                while st and st[-1] > 0 and st[-1] < abs(asteroids[i]):

                    # Destroy the asteroid
                    st.pop()

                # If there is right moving asteroid
                # which is of same size
                if st and st[-1] == abs(asteroids[i]):

                    # Destroy both the asteroids
                    st.pop()

                # Otherwise, if there is no left
                # moving asteroid, the right moving
                # asteroid will not be destroyed
                elif not st or st[-1] < 0:

                    # Storing the array in final state
                    st.append(asteroids[i])

        # Return the final state of asteroids
        return st