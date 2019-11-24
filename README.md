# sli-metrics
Prometheus metrics for platform SLI. 

Simply drop files into the **/metrics** folder.

* The extension must be _.metric_
* The name oof the file becomes the metric name
    > Remember Prometheus metric naming conventions and restrictions.

* The contents of the file must take the following form
    >Note: each element must be seperated by a semi-colon (;)
    1. Metric description
    2. Metric type (counter, gauge etc)
    3. Additional comment
    4. Metric labels
    5. Metric value

### Example file contents

```

this is a cool another metric;counter;This is a comment;cluster="test-cluster.domain", host="my-host-1.domain";123
this is a cool another metric;counter;This is a comment;cluster="test-cluster.domain", host="my-host-2.domain";2345
this is a cool another metric;counter;This is a comment;cluster="test-cluster.domain", host="my-host-3.domain";1124

```

See [here](sli-metrics/metrics) for more examples

## Building the Container
```
docker build --tag sli-metrics .
docker run --name sli_metrics  -d -p 5000:80 sli-metrics:latest
```