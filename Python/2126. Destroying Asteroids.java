class Solution {
    /**
     * Determines if a planet can destroy all asteroids by absorbing their mass.
     * The planet can only destroy asteroids with mass less than or equal to its current mass.
     * After destroying an asteroid, the planet's mass increases by the asteroid's mass.
     * 
     * @param mass Initial mass of the planet
     * @param asteroids Array of asteroid masses to be destroyed
     * @return true if all asteroids can be destroyed, false otherwise
     */
    public boolean asteroidsDestroyed(int mass, int[] asteroids) {
        // Sort asteroids in ascending order to tackle smaller ones first
        Arrays.sort(asteroids);
      
        // Use long to prevent integer overflow as mass accumulates
        long currentMass = mass;
      
        // Iterate through each asteroid in sorted order
        for (int asteroidMass : asteroids) {
            // Check if current mass is sufficient to destroy this asteroid
            if (currentMass < asteroidMass) {
                return false;  // Cannot destroy this asteroid, mission fails
            }
          
            // Absorb the asteroid's mass after destroying it
            currentMass += asteroidMass;
        }
      
        // All asteroids successfully destroyed
        return true;
    }
}
