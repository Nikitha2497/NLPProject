import logging
from typet5.data import GitRepo

def count_repo_annots(rep, repos_dir):
    try:
        rep.collect_annotations(repos_dir)
        if rep.n_type_annots / rep.lines_of_code > 0.05:
            return rep
    except Exception as e:
        logging.warning(f"Failed to count annotations for {rep.name}. Exception: {e}")
        return None

