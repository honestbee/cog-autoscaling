# Autoscaling cog bundle

This is a bundle to run in Operable Cog to manage AWS autoscaling groups.

Available commands : 

`autoscaling:group list` : lists autoscaling groups by name.

`autoscaling:group scale -n [autoscaling group name] -t [elastic beanstalk tag] -d [number of instances]`: scales an autoscaling group based on its name or `elasticbeanstalk:environment-name` tag. Use -n or -t, not both together.
