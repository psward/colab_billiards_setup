def setup():
  if clone_repo:
      repo_name = 'billiard_frontiers'
      user_name = 'drscook'
      repo_url = f"https://github.com/{user_name}/{repo_name}.git"
      cmd = f"PATH=$PATH:/bin; PATH=$PATH:/usr/bin; cd {repo_path};"  
      rtn = os.system(cmd + f"git pull")
      if rtn == 0:
          print(f"Repo {repo_name} successfully updated")
      else:
          print(f"Could not update repo {repo_name}.  Trying to clone.")
          os.makedirs(repo_path, exist_ok=True)
          rtn = os.system(cmd + f"git clone {repo_url} {repo_path}")
          if rtn == 0:
              print(f"Repo {repo_name} successfully cloned")
          else:
              print(f"Could neither update nor clone {repo_name}.  Attempting to proceed anyway.  Fingers crosses.")



  ## Required - loads essentials
  os.chdir(root_path)
  # Import external packages, display preferences, utilities, billiard defintions
  files = [['setup', ['imports_preferences_utilities', 'setup_pkgs']]
          ,['definitions', ['constants_global_defaults', 'meshes'
                            ,'no_slip_functions', 'pw_collision_laws', 'pp_collision_laws'
                           ,'walls', 'chambers', 'particles']]
          ,['dynamics', ['evolution', 'solver_cpu', 'gpu', 'solver_gpu']]
          ,['analysis', ['analyses', 'animate']]
       ]
  for x in files:
      subdir = x[0]
      for fn in x[1]:
          y = subdir + '/' + fn
          z = repo_path + y
          %run -i "{z}"
          print(f"Successfully imported {y}.py")

  if setup_for_parallel_mode: 
      setup_gpu()  # if you plan to run in parallel


  if setup_for_animation_file:
      setup_ffmpeg()
