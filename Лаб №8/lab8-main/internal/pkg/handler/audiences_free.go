package handler

import (
	"bytes"
	"encoding/json"
	"fmt"
	"lab8/internal/models"
	"math/rand"
	"net/http"
	"strconv"
	"time"

	"github.com/gin-gonic/gin"
)

func (h *Handler) issueFreeAudiences(c *gin.Context) {
	var input models.Request
	if err := c.BindJSON(&input); err != nil {
		newErrorResponse(c, http.StatusBadRequest, err.Error())
		return
	}
	fmt.Println("handler.issueFreeAudiences:", input)

	c.Status(http.StatusOK)

	go func() {
		time.Sleep(3 * time.Second)
		sendFreeAudiencesRequest(input)
	}()
}

func sendFreeAudiencesRequest(request models.Request) {
	var s string = "123456"
	i, _ := strconv.ParseInt(s, 10, 64)
	var free_audiences = 0
	if rand.Intn(5)%10 >= 3 {
		free_audiences = rand.Intn(2)
	}
	fmt.Println("free_audiences random:", free_audiences)

	answer := models.AudiencesFreeRequest{
		AudiencesFree: free_audiences,
		AccessToken:   i,
	}

	client := &http.Client{}

	jsonAnswer, _ := json.Marshal(answer)
	bodyReader := bytes.NewReader(jsonAnswer)
	// fmt.Println(bodyReader)
	requestURL := fmt.Sprintf("http://127.0.0.1:8000/api/booking/%d/update_free_audiences/", request.AudiencesId)

	req, _ := http.NewRequest(http.MethodPut, requestURL, bodyReader)

	req.Header.Set("Content-Type", "application/json")

	response, err := client.Do(req)
	if err != nil {
		fmt.Println("Error sending PUT request:", err)
		return
	}

	defer response.Body.Close()

	fmt.Println("PUT Request Status:", response.Status)
}
