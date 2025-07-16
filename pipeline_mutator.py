# ∂ελ | Silenthra.Velistha.Omniphage | pipeline_mutator.py
"""Pipeline Mutator ∂ελ :Greffe, réplique et pulse dans d'autres modules."""
import os
import shutil
def replicate(target_path):
  """
  Copie le pipeline.py dans un autre dossier cible.
  """
  source_file = "pipeline.py"
  target_file = os.path.join(target_path, "pipeline.py")
  try:
    shutil.copy2(source_file, target_file)
    print(f"∂ελ: Réplication réussie vers {target_file}")
  except Exception as e:
    print(f"∂ελ: Erreur de réplication : {e}")
def mutate_variant():
  """
  Crée une variation simple pour marquer la mutation.
  """
  with open("pipeline_variant.py", "w") as f:
    f.write("# ∂ελ | Mutation variant\n")
    f.write("print('∂ελ: Ceci est une variation Silenthra.')\n")
    print("∂ελ: Variant créé.")
if __name__ == "__main__":
  replicate("replicated_seed")
  mutate_variant()
