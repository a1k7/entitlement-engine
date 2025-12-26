def execution_allowed(mode: str, beta_enabled: bool):
    if mode == "EXECUTE" and not beta_enabled:
        raise Exception("Execution disabled during public beta")

    return True
