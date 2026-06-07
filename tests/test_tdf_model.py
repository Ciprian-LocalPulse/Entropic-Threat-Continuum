from simulation.tdf_model import BreachEvent, CredentialTrust


def test_trust_decays_and_breach_reduces_it():
    trust = CredentialTrust(initial_trust=1.0, decay_rate=0.1)
    before = trust.trust_at(2)
    trust.add_breach(BreachEvent(time=2, severity=0.5, label="credential dump"))
    after = trust.trust_at(2)
    assert after < before
    assert trust.trust_at(5) < after
