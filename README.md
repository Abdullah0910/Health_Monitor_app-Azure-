                                                              Health Monitor App
A lightweight Flask-based health dashboard simulating services in a POS system, with Prometheus integration and cloud deployment support

                                                                  Features
--Service health simulation (POS_API, PaymentGateway, InventoryService)
--Prometheus metrics on /metrics
--Health check on /health
--Dockerized for easy deployment

                                                              Run with Docker
docker build -t health-monitor . ##these commands in bash
docker run -p 5000:5000 health-monitor

                                                   Now Finally Deploy to Azure App Service


1. az login

2. az group create --name health-monitor-rg --location westeurope

3. az appservice plan create --name health-monitor-plan --resource-group health-monitor-rg --is-linux --sku B1

4.az webapp create --resource-group health-monitor-rg --plan health-monitor-plan --name <Healthmonitor> --deployment-container-image-name health-monitor

5. az webapp config container set --name <your-app-name> --resource-group health-monitor-rg --docker-custom-image-name <abdullah0904>/health-monitor



                                                          Prometheus Configuration
Prometheus can scrape the metrics at /metrics to monitor request counts
   global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'health-monitor-app'
    static_configs:
      - targets: ['localhost:5000']  # Or your cloud URL/IP
   
    
      - <img width="959" alt="image" src="https://github.com/user-attachments/assets/9972ade9-837e-49f2-884b-2d1f439cd8ba" />


----------------------------------------------Thanks-----------------------------------------
