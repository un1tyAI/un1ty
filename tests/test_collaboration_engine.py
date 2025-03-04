import un1ty
import pytest

def test_combine_outputs():
    """Test if the Collaboration Engine correctly combines AI-generated outputs."""
    shapesh1ft_output = "Quantum computing is a fascinating field."
    gh0st_output = "Quantum computing utilizes qubits to perform computations faster."
    
    combined_output = un1ty.collaborate(creative_text=shapesh1ft_output, summary=gh0st_output)
    
    assert isinstance(combined_output, str)
    assert "Quantum computing" in combined_output
    assert len(combined_output) > len(gh0st_output)  # Ensuring enhancement occurs

if __name__ == "__main__":
    pytest.main()