"""
Execute all session notebooks with the provided OpenAI credentials.
Saves executed notebooks with outputs in-place.
"""
import os
import sys
import nbformat
from nbclient import NotebookClient

# Set environment variables so all notebooks pick them up
os.environ["OPENAI_API_KEY"] = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyZTc5YTE4MS1jNGViLTQ2NjUtOWJhNy03MTQzM2MyMmY2ZWQiLCJleHAiOjE3NzY0NzYyNzIsImlhdCI6MTc3NjQzMzA3MiwianRpIjoiMWYxNjBjMmMtYTVlZC00NjJkLThiY2QtNTUzMTM5ZjYzY2MzIiwidHlwZSI6ImFjY2VzcyIsImlzcyI6ImNoYXQtcHJveHktYXBpIiwiYXVkIjoiY2hhdC1wcm94eS11c2VycyIsImVtYWlsIjoidEB0LmNvbSJ9.1-KbLGCrR3YTYxonDbeg-MkaJ68MDne1djRd5hUfVvw"
os.environ["OPENAI_BASE_URL"] = "http://localhost:8001/v1"
os.environ["OPENAI_MODEL"] = "gpt-5-mini"

WORKSPACE = os.path.dirname(os.path.abspath(__file__))

# Session 9 interactive cell replacement (use predefined queries instead of input())
SESSION_9_INTERACTIVE_REPLACEMENT = '''# Demo queries (non-interactive version for batch execution)
assistant.reset()

print("=" * 50)
print("TechNova Smart Assistant")
print("=" * 50)

demo_queries = [
    "What products does TechNova offer?",
    "How does the ProMax compare to competitors?",
    "Calculate the price difference between ProMax and the budget option",
]

for query in demo_queries:
    print(f"\\nYou: {query}")
    response = assistant.chat(query)
    print(f"\\nAssistant: {response}")

print("\\nGoodbye!")
'''

NOTEBOOKS = [
    "session_1_llm_api_fundamentals.ipynb",
    "session_2_prompt_engineering.ipynb",
    "session_3_structured_outputs.ipynb",
    "session_4_embeddings_semantic_search.ipynb",
    "session_5_rag.ipynb",
    "session_6_function_calling.ipynb",
    "session_7_building_agents.ipynb",
    "session_8_advanced_patterns.ipynb",
    "session_9_capstone.ipynb",
]

def patch_interactive_cells(nb, notebook_name):
    """Replace interactive input() cells with predefined queries."""
    if notebook_name == "session_9_capstone.ipynb":
        for cell in nb.cells:
            if cell.cell_type == "code" and "input(" in cell.source:
                print(f"  -> Patching interactive cell in {notebook_name}")
                cell.source = SESSION_9_INTERACTIVE_REPLACEMENT
    return nb

def run_notebook(notebook_path, notebook_name):
    """Execute a notebook and save it with outputs."""
    print(f"\n{'='*60}")
    print(f"Running: {notebook_name}")
    print(f"{'='*60}")
    
    nb = nbformat.read(notebook_path, as_version=4)
    nb = patch_interactive_cells(nb, notebook_name)
    
    client = NotebookClient(
        nb,
        timeout=300,  # 5 min per cell
        kernel_name="python3",
        resources={"metadata": {"path": WORKSPACE}},
    )
    
    try:
        client.execute()
        print(f"  SUCCESS: {notebook_name}")
    except Exception as e:
        print(f"  ERROR in {notebook_name}: {e}")
        # Still save partial results
    
    # Save the notebook with outputs
    nbformat.write(nb, notebook_path)
    print(f"  Saved: {notebook_path}")

def main():
    failed = []
    succeeded = []
    
    for nb_name in NOTEBOOKS:
        nb_path = os.path.join(WORKSPACE, nb_name)
        if not os.path.exists(nb_path):
            print(f"SKIP: {nb_name} not found")
            continue
        try:
            run_notebook(nb_path, nb_name)
            succeeded.append(nb_name)
        except Exception as e:
            print(f"FATAL ERROR with {nb_name}: {e}")
            failed.append((nb_name, str(e)))
    
    print(f"\n{'='*60}")
    print(f"SUMMARY")
    print(f"{'='*60}")
    print(f"Succeeded: {len(succeeded)}/{len(NOTEBOOKS)}")
    for name in succeeded:
        print(f"  ✓ {name}")
    if failed:
        print(f"Failed: {len(failed)}/{len(NOTEBOOKS)}")
        for name, err in failed:
            print(f"  ✗ {name}: {err}")

if __name__ == "__main__":
    main()
