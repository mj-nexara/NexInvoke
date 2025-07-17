$headers = @{
    "Content-Type" = "application/json"
}

$body = @{
    message = "What is Nexara Protocol?"
}

$response = Invoke-RestMethod -Uri "http://127.0.0.1:8000/invoke" `
    -Method Post `
    -Headers $headers `
    -Body ($body | ConvertTo-Json -Depth 3)

$response.choices[0].message.content