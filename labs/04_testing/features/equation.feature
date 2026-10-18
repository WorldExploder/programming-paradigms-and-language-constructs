Feature: Biquadratic equation
  Scenario: Four real roots
    Given coefficients 1, -5, 4
    When I solve the equation
    Then the roots are -2, -1, 1, 2

  Scenario: No real roots
    Given coefficients 1, 0, 1
    When I solve the equation
    Then there are no real roots

  Scenario: Repeated roots
    Given coefficients 1, -2, 1
    When I solve the equation
    Then the roots are -1, 1
