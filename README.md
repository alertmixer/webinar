Мои хинты с вебинара:
```
export KUBECONFIG=~/Downloads/k8s-1-16-6-do-0-sfo2-1583303047581-kubeconfig.yaml
```

```
helm repo add stable https://kubernetes-charts.storage.googleapis.com/
```

```
helm fetch stable/prometheus --untar
```

```
helm install ./prometheus --generate-name
```

```
kubectl get service -o yaml
```

Ладно, и этот башник тоже:
```
kubectl get nodes -o wide | awk '{print $7":9100"}' | xargs -n11 | sed "s/ /\',\'/g"
```

```
helm create load-app
```

```
docker tag load motakukk/webinar-k8s-load:latest
```

```
docker push motakukk/webinar-k8s-load:latest
```

```
helm list --all
```

```
helm upgrade load-app-1583315661 ./load-app/
```
