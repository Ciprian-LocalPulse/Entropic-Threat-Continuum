from simulation.aeg_model import AdversarialEntropyGradient, EntropyObservation


def test_aeg_gradient_is_positive_when_entropy_falls():
    model = AdversarialEntropyGradient(
        [
            EntropyObservation(0, 10),
            EntropyObservation(1, 8),
            EntropyObservation(2, 5),
        ]
    )
    assert model.mean_gradient() > 0
    assert model.predict(3) >= 0
